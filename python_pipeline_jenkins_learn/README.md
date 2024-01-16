## How start using fastapi
```
uvicorn main:app --reload
```


## How run tests
Go to the folder `/Users/paulo.mulotto/Codes/learn/jenkins_learn/python_pipeline_jenkins_learn` and run `pytest`

Not integration tests:
pytest -m "not integtest"

Integration tests:
pytest -m integtest