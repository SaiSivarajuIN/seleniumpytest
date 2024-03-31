

pip install selenium
pip install pytest
pip install pytest-html


pytest --browser_name edge
py.test --html=./reports/report.html
pytest --browser_name edge --html=./reports/report1.html

jenkins junit result publish
py.test --html=./reports/report.html -v --junitxml="result.xml"


pytest --alluredir=%allure_result_folder% ./tests
allure serve %allure_result_folder%


