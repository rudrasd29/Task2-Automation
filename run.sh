#pytest testCases/Test.py
pytest --cache-clear -s -v --html=Reports/report.html testCases/Test.py
#pytest --cache-clear -s -v --html=Reports/report.html testCases/Test.py --browser firefox