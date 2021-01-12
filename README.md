build the project
=================

```
conan export utils.py devops/testing
conan create day01.py devops/testing --profile <profile> --build=missing
```
