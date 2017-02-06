
# 4 Basic Data Types: Lists and Tuples

<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

* [4 Basic Data Types: Lists and Tuples](#4-basic-data-types-lists-and-tuples)
  * [4.1 Lists](#41-lists)
    * [4.1.1 Sequence Operations on Lists](#411-sequence-operations-on-lists)
    * [4.1.2 List Methods](#412-list-methods)
    * [4.1.3 The Built-in range Function](#413-the-built-in-range-function)
    * [4.1.4 Copying a List](#414-copying-a-list)
    * [Shallow Copy](#shallow-copy)
    * [Deep Copy](#deep-copy)
  * [4.2 Tuple](#42-tuple)
  * [4.3 Syntax Check and Tracebacks](#43-syntax-check-and-tracebacks)
  * [4.4 Key Terms](#44-key-terms)
  * [4.5 Exercises](#45-exercises)

<!-- tocstop -->

## 4.1 Lists

```python
fields = ['FireId', 'Org', 'Reg-State', 'FireType']
fields
```




    ['FireId', 'Org', 'Reg-State', 'FireType']




```python
stateData = ['Florida', ['Alabama', 'Georgia'], 18809888]
stateData
```




    ['Florida', ['Alabama', 'Georgia'], 18809888]




```python
exampleList = [10000, 'a', 1.5, 'b', 'banana', 'c', 'cusp']
exampleList
```




    [10000, 'a', 1.5, 'b', 'banana', 'c', 'cusp']




```python
dataList = []
```

### 4.1.1 Sequence Operations on Lists


```python
exampleList = [10000, 'a', 1.5, 'b', 'banana', 'c', 'cusp']
exampleList[0] = 'prune'# modifying the first item in the list.
exampleList
```




    ['prune', 'a', 1.5, 'b', 'banana', 'c', 'cusp']



### 4.1.2 List Methods


```python
# Initialize the list with 4 IDs.
fireIDs = ['238998', '239131', '239135', '239400']
newID = '239413'
fireIDs.append(newID) # Changing the list in-place.
fireIDs
```




    ['238998', '239131', '239135', '239400', '239413']



### 4.1.3 The Built-in range Function


```python
range(9)
```




    [0, 1, 2, 3, 4, 5, 6, 7, 8]




```python
range(5,9)
```




    [5, 6, 7, 8]




```python
range(0,9,2)
```




    [0, 2, 4, 6, 8]



### 4.1.4 Copying a List


```python
fireIDs = ['238998', '239131', '239135', '239400']
fireIDs.reverse()
fireIDs
```




    ['239400', '239135', '239131', '238998']



### Shallow Copy


```python
a = range(1,11)
a
```




    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]




```python
b = a# "shallow copy" list a
b
```




    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]




```python
a.reverse()# reverse list a
a
```




    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]




```python
b
```




    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]



---

### Deep Copy


```python
a = range(1,11)
a
```




    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]




```python
b = list(a)# "deep copy" list a
b
```




    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]




```python
a.reverse()# reverse list a
a
```




    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]




```python
b
```




    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]



## 4.2 Tuple


```python
t = "abc", 456, 'wxyz'
type(t)
```




    tuple




```python
t
```




    ('abc', 456, 'wxyz')




```python
t2 =(4.5, 7, 0.3)
type(t2)
```




    tuple




```python
t2
```




    (4.5, 7, 0.3)



---


```python
t[0]
```




    'abc'




```python
t[1]
```




    456




```python
t2[0]
```




    4.5




```python
t2[0] = 5
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-34-a91a1e24869f> in <module>()
    ----> 1 t2[0] = 5


    TypeError: 'tuple' object does not support item assignment


## 4.3 Syntax Check and Tracebacks

## 4.4 Key Terms

## 4.5 Exercises


```python

```
