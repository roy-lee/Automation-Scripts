# How to download extremely large file on Google Drive

## Motivation

This script was created as I happened to have the need to download a 124GB file on Google Drive.

## Relevant Links

[Instructions](https://www.quora.com/How-do-I-download-a-very-large-file-from-Google-Drive?share=1)

[Google Auth](https://developers.google.com/oauthplayground/)

[Google Drive](https://drive.google.com/drive/folders/1ADcZugpo8Z6o5q1p2tIAibwhsL8DcVwH)

### TL;DR:
 
1. Get ```FILEID``` for the file you need from GoogleDrive.
2. Get your ```TOKEN``` from DriveV3 readonly API
3. Replace ```TOKEN``` and ```FILEID``` into ```googleDrive-download-script.sh```
4. Run ```./googleDrive-download-script.sh``` from your terminal (Make sure you have enough storage space in your disk)

---

**FILEID** : ```XXXXX```

**TOKEN** : ```YYYYY```

**FILENAME** : ```ZZZZZ```

**FORMAT**:

```bash
curl --retry 999 --retry-delay 5000 -C - -H "Authorization: Bearer YYYYY" https://www.googleapis.com/drive/v3/files/XXXXX?alt=media -o ZZZZZ
```

#### Notes:
[--retry 999](https://curl.haxx.se/docs/manpage.html#--retry) 

[--retry-delay 5000](https://curl.haxx.se/docs/manpage.html#--retry-delay) 

[-C -](https://curl.haxx.se/docs/manpage.html#-C)

---

##### Examples

File : ```testdata.tar.gz``` [69GB]

Link : https://drive.google.com/file/d/1wZVZjTwiAKiE2h_yrdi2C_ip8PqVygaJ/view?usp=sharing

Command: 

```bash
curl -H "Authorization: Bearer YYYYY" https://www.googleapis.com/drive/v3/files/1wZVZjTwiAKiE2h_yrdi2C_ip8PqVygaJ?alt=media -o testdata.tar.gz
```

---

File : ```train_celebrity.tar.gz``` [91GB]

Link : https://drive.google.com/file/d/15UMoAQvJN38VcENuNvtOGfj2U8pkL_0z/view?usp=sharing

Command: 
```bash
curl -H "Authorization: Bearer YYYYY" https://www.googleapis.com/drive/v3/files/15UMoAQvJN38VcENuNvtOGfj2U8pkL_0z?alt=media -o train_celebrity.tar.gz
```

---

File : ```train_msra.tar.gz``` [125GB]

Link : https://drive.google.com/file/d/1JL6zBHgrQP0xJRR_fDBPu7R3txqRpQKu/view?usp=sharing

Command:
```bash 
curl -H "Authorization: Bearer YYYYY" https://www.googleapis.com/drive/v3/files/1JL6zBHgrQP0xJRR_fDBPu7R3txqRpQKu?alt=media -o train_msra.tar.gz
```

---

##### Issues

Some errors faced:

1. curl: (18) transfer closed with 68780341771 bytes remaining to read
 
    - Possible to continue by re-running the script

2. curl: (33) HTTP server doesn't seem to support byte ranges. Cannot resume.

    - **Fatal error**, impossible to continue. Delete file and restart the script.

3. curl: (56) OpenSSL SSL_read: Connection was reset, errno 10054

    - Possible to continue by re-running the script