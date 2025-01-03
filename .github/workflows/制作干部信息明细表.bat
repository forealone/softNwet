@echo off
setlocal enabledelayedexpansion
e:
cd E:\
cd 23-个人

python MonthlyReport_main.py

echo 执行python脚本(MonthlyReport_main.py)结束。

python CadreInfoSheet.py

echo 执行python脚本(CadreInfoSheet.py)结束。

python CadreChangeSheet.py

echo 执行python脚本(CadreChangeSheet.py)结束。

python StatisticalTable.py

echo 执行python脚本(StatisticalTable.py)结束。

python InfoSheetLayout.py

echo 执行python脚本(InfoSheetLayout.py)结束。

python ChangeSheetLayout.py

echo 执行python脚本(ChangeSheetLayout.py)结束。

python InfoSheetLite.py

echo 执行python脚本(InfoSheetLite.py)结束。

python ChangeSheetLite.py

echo 执行python脚本(ChangeSheetLite.py)结束。

set /a seconds=5
:countdown
echo !seconds! 秒后关闭...
timeout /t 1 >nul
set /a seconds-=1
if !seconds! gtr 0 goto countdown