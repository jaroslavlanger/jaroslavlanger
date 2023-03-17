# tqdm

`tqdm` derives from the Arabic word taqaddum (تقدّم) which can mean “progress,” and is an abbreviation for “I love you so much” in Spanish (te quiero demasiado).

```sh
pip3 install tqdm
```

```py
from tqdm import tqdm

iterator = range(10)    # it can be anything

for elem in tqdm(iterator):
    print('This progress si beautifully visualized')
```

