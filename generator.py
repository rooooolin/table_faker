import cfg_load
import pandas as pd
from loguru import logger
from utils import find_files,create_folder
import os
import shutil
from modules import build_table,build_datarule
import random

class Genreator:
    def __init__(self,args) -> None:
        super().__init__()
        self.args = args
        #self.tables = cfg_load.load(args.config)

    def write_markdown(self):
        markdown_str=''
        pkls = find_files(self.args.work_dir+"/tmp/",['.pkl'])
        for pkl in pkls:
            table_name = os.path.basename(pkl).strip('.pkl')
            pkl = pd.read_pickle(pkl)

            markdown_str+=f'### {table_name}\n\n'
            markdown_str += pkl.to_markdown(index=False, tablefmt="pipe", headers="keys")
            markdown_str+='\n\n\n\n'

        markdown_str = markdown_str.replace('|-', '|:-').replace('-|', '-:|')

        with open(f'{self.args.work_dir}/rst.md','w',encoding='utf-8') as f:
            f.writelines(markdown_str)
        print(f"write markdown to  {self.args.work_dir}/rst.md")

    def parse_out_values(self,out_tables,tns,fake_amount):
        fvs=dict()
        for tn in out_tables:
            tn_pkl = self.args.work_dir+"/tmp/"+tn+".pkl"
            if not os.path.isfile(tn_pkl):
                raise FileNotFoundError(f'table {tn} must come before {" and ".join(tns)} in yaml')
            pkl =pd.read_pickle(tn_pkl)
            data = pkl.to_dict(orient='list')
            data.update({"ris":[random.randint(0,len(pkl)-1) for _ in range(fake_amount)]})
            fvs.update({tn:data})
        return fvs
    
    def fakedata(self,fields,fvs,i):
        values = []
        
        for fn,dr in fields.items():
            if isinstance(dr,list):
                out_tn = dr[1]
                dr = dr[0]
            dr = dr.upper()
            if 'INT' in dr or 'FLOAT' in dr:
                _type,interval = dr.split('(')
                interval = list(map(float,interval.strip(')').split(',')))
                val = self.data_rules['NUMERICAL'](_type=_type,low=interval[0],high=interval[1])
            elif dr == 'OUT':
                val = fvs[out_tn][fn][fvs[out_tn]['ris'][i]]
            else:
                val = self.data_rules[dr](index = i, fsv = fvs, hg = dict(zip(list(fields.keys())[:len(values)],values)))
            
            values.append(val)
        return values
    
    def merge_table(self,tables):
        mt =[]
        def find_tn(matrix, target):
            for i, row in enumerate(matrix):
                if target in row:
                    return i
            return None
        for tn,table in tables.items():
            et = table.table['et']
            if not et:
                mt.append([tn])
            else:
                i= find_tn(mt,et)
                if i:
                    mt[i].append(tn)
        return mt
    
    def append_dt(self, od, key, nv):
        od.setdefault(key, [])
        od[key] = list(set(od[key] + nv))

    def append_field(self,od, nd):
        for k, v in nd.items():
            dr = None
            if isinstance(v, list):
                if len(v) ==2:
                    if v[1] == 'primary':
                        dr = v[0]
                    else:
                        dr=v
            else:
                dr = v
            if dr:
                if k not in od:
                    od[k] = dr
                else:
                    if od[k] != dr:
                        raise NameError(f'there are two different data_rule {od[k]} and {dr} at the same the field {k}.')

    def run(self):
        create_folder(self.args.work_dir)
        config= cfg_load.load(self.args.config)
        logger.add(self.args.work_dir+"/log.log")
        shutil.copy(self.args.config,self.args.work_dir)
        logger.info('build tables..')
        tables = build_table(config['table'])
        mt =self.merge_table(tables=tables)

        self.data_rules = build_datarule(config['datarule'])
        logger.info('fake datas..')

        for tns in mt:
            rsts=[]
            fields={}
            dts = {}
            fas =[]
            for tn in tns:
                self.append_field(fields,tables[tn].table['fields'])
                dt =tables[tn].table['dt']
                fas.append(tables[tn].table['fake_amount'])
                for k,v in dt.items():
                    self.append_dt(dts, k, v) 
            fa= max(fas)
            fvs=None if not dts else self.parse_out_values(dts,tns,fa)
            for i in range(fa):
                rsts.append(self.fakedata(fields,fvs,i))
            df=pd.DataFrame(
                {k: v for k, v in zip(fields, zip(*rsts))}
                )

            for tn in tns:
                tn_fields = tables[tn].table['fields']
                tn_fa = tables[tn].table['fake_amount']
                tn_df = df[list(tn_fields)].head(tn_fa)
                pkl = self.args.work_dir+"/tmp/"+tn+".pkl"
                tn_df.to_pickle(pkl)
                logger.success(f"Generate {tn_fa} data of table:{tn}")
        self.write_markdown()

      
      
           