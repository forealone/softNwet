@echo off
setlocal enabledelayedexpansion
e:
cd E:\
cd 23-����

python MonthlyReport_main.py

echo ִ��python�ű�(MonthlyReport_main.py)������

python CadreInfoSheet.py

echo ִ��python�ű�(CadreInfoSheet.py)������

python CadreChangeSheet.py

echo ִ��python�ű�(CadreChangeSheet.py)������

python StatisticalTable.py

echo ִ��python�ű�(StatisticalTable.py)������

python InfoSheetLayout.py

echo ִ��python�ű�(InfoSheetLayout.py)������

python ChangeSheetLayout.py

echo ִ��python�ű�(ChangeSheetLayout.py)������

python InfoSheetLite.py

echo ִ��python�ű�(InfoSheetLite.py)������

python ChangeSheetLite.py

echo ִ��python�ű�(ChangeSheetLite.py)������

set /a seconds=5
:countdown
echo !seconds! ���ر�...
timeout /t 1 >nul
set /a seconds-=1
if !seconds! gtr 0 goto countdown