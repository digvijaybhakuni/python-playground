# Python Playgroud 

This sample python leaning playground for me


Test Edit
## Setting up virtual enviroment 

To install virtuals enviroment

```
python -m pip install virtualenv

```

To setup enviroment

virtualenv -p <python version path> <env name>

```
virtual -p /usr/bin/python3 test_env
```

To activate the enviroment 

```
source test_env/bin/activate
```

To install lib in this env.


```
pip install numpy
```


Get all the requirment 

```
pip freeze --local > requirement.txt

```   

To deactivate env.

```
deactivate
```

To remove env.

```
rm -rf test_env
```

To install lib install env. from requirements.txt

```
pip install -r requirement.txt
```

