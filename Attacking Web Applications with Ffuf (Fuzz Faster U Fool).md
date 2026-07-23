# **Attacking Web Applications with Ffuf (Fuzz Faster U Fool)**
# **Introduction:**
### Fuzzing:
Fuzzing is the process of providing a web application or software with many different inputs to observe how it responds and to identify unexpected behavior, hidden resources, or potential vulnerabilities.

Is fuzzing limited to directories only?
No, many things should be fuzzed 

1. Directories

```
/admin
/login
/uploads
```
---
2. Files

```
config.php
backup.zip
robots.txt
```

---

3. Parameters

```
?id=1
?debug=true
?admin=1
```

---

4. Headers

```
User-Agent
Host
X-Forwarded-For
```

---

5. Subdomains

```
admin.example.com
api.example.com
dev.example.com
```

---

### What does FFUF do?

If we use a command:

```
ffuf -u http://target/FUZZ -w wordlist.txt
```

Then: 

**FFUF (Fuzz Faster U Fool) replaces the `FUZZ` keyword with every word from the wordlist and sends a request for each one. It then checks:**

- Which requests returned a **200 OK** status code?
- Which responses have a different size?
- Which requests produced an interesting or unexpected response?