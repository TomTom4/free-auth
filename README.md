# FastAuth
a free authentication and authorization server, based on FastApi, SQLModel and jwcrypto.


## Generate key pair

```bash
# generate a private key
openssl ecparam -name secp521r1 -genkey -noout -out private.pem

# extract the public key
openssl ec -in private.pem -pubout -out public.pem
```

# start
```bash
uvicorn src.main:app --reload
```
