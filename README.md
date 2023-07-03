一个用于测试人员快速生成测试表数据的框架

- [x] 支持自定义【表名】，【字段名】，【表数量】，【字段数量】
- [x] 支持自定义【字段的数据规则】，且支持扩展【数据规则】
- [x] 支持【表间】字段关联，支持【表内】字段关联
- [x] 支持【表与表】的关联（如：某表的详细表）
- [x] 提供以下内置数据规则（不区分大小写）：
    - [x] 自增ID（INCREMENTID） / UUID（uuid）
    - [x] 随机中文名（CHINESENAME），公司名（COMPANYNAME），电子设备名称（ee）
    - [x] 随机地址（address），随机手机号码（tel）
    - [x] 随机日期（date），关联随机日期(外链表的字段)的收货日期（receiptdate），关联随机日期(外链表的字段)的开票日期（invoicedate）
    - [x] 带区间的随机数值（float,int）（float(xx,xx),int(xx,xx)）
    - [x] 关联物品(表内字段)的价格（price），单位（unit）
- [x] 支持写入结果到【Markdwon】
  
## 使用方法

### 1，配置文件

新建.yaml文件，内容格式为dict，必须包含table和datarule两个key。table和datarule均为list，list中包含若干表定义及数据规则定义。

```
{
  "table":[...]
  "datarule":[...]
}
```

#### 1.1 table的定义
每张表为一个dict，必须包含以下4个key。
|   key | value类型         |   备注 | 
|:------------:|:--------------------:|:-------------:|
|class_ | str | 表初始化时所执行的类（定义类时必须继承BaseTable类） |
|name | str |表名，需唯一 |
|fields | dict |字段。存在以下四种表达格式：<br>1）一般表达格式为 字段名:数据规则<br>2）若该field为主键，则 字段名:[数据规则,"primary"]<br>3）若该字段的值来源于其他表，则 字段名:["out",表名]<br>4）若该字段的值来源于其他表，同时又是主键，则 字段名:["out",表名,"primary"] |
|fake_amount | int |            需要生成的记录数量 |
|... | ... |            其他自定义属性 |


#### 1.2 datarule的定义
每个datarule为一个dict，必须需要包含以下2个key
|   key | value类型         |   备注 | 
|:------------:|:--------------------:|:-------------:|
|  class_ | str | 定义规则所执行的类 |
|  name | str | 规则名称 |
|           ... | ... |            其他自定义属性 |

### 2，执行

```python run.py --config /path/to/yaml --work_dir /path/to/save/result```

## 扩展数据规则

>1) 在 modules/datarules/ 下新建.py文件

>2) 自定义类并注册类，同时需继承BaseDataRule类。

>3) 定义run方法，并在run方法内部返回结果。

>4) 在配置文件上中的datarule中按照1.2中定义添加数据规则。

## TODO

- [ ] 支持写入结果到 Excel & Mysql
- [ ] 支持多进程。
