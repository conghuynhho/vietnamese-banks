## List Viet Nam Banks & Bank Branches

Using api of Shopee to get list of banks and bank branches in Viet Nam.

#### Requirements
- Python
- Requests
- Json


#### Usage
1. Get list of banks

```python
python get_banks.py
```

2. Get list of bank branches

```python
python get_bank_branches.py
```

#### Notes
You need to pass authorization to using api of Shopee. You can get it by using Chrome DevTools.
Create `cookie.py` and export `cookie` variable.

```python
cookie = {
  # your cookie
}
```

#### Output
It will create 2 files: `banks.json` and `bank_branches.json` in the same folder.



