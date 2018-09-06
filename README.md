# OpenID Connect Sample

## Run servers & Initialize

```
cd openid-connect-sample
./run.sh
```

## Edit hosts
```
sudo sh -c "echo 127.0.0.1 op.local >> /etc/hosts"
sudo sh -c "echo 127.0.0.1 rp1.local >> /etc/hosts"
sudo sh -c "echo 127.0.0.1 rp2.local >> /etc/hosts"
```

## How to check behavior

1. If you open "http://rp1.local/", it will be redirected to "http://op.local/login/".
2. Login to "http://op.local/login/".
3. Open "http://rp2.local". You can see that you are already logged in.
4. If you click the logout button of "http: //rp2.local/", it will be redirected to "http://op.local/logout/"
5. Open "http://rp1.local". You can see that you are already logged out.

