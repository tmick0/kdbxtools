# kdbxtools

A collection of CLI tools for dealing with Keepass (KDBX) databases. 

Inspired by [kdbxpasswordpwned](https://github.com/fopina/kdbxpasswordpwned), this is intended to be used in a workflow to check your password DB against the breached password lists provided by [Have I Been Pwned](https://haveibeenpwned.com/Passwords).

```bash
pip install .
kdbx2csv ~/my_keepass_db.kdbx my_keepass_hashes.csv
sort my_keepass_hashes.csv > my_keepass_hashes_sorted.csv
checkhashes my_keepass_hashes_sorted.csv pwned-passwords-sha1-ordered-by-hash-v7.txt
```

Note that both the `kdbx2csv` file and the HIBP dump need to be pre-sorted on the hash. The dump is available in this form from the link above, but currently kdbx2csv does not sort its output.

## kdbx2csv 

Exports a CSV containing SHA1 hashes of all passwords, with columns `sha1, username, title`. Allows a keyfile to be optionally passed as an argument, and prompts interactively for the master password.

## checkhashes

Identifies matches between a sorted `kdbx2csv` CSV and the sorted hash dump provided by HIBP. Produces a CSV of compromised passwords with columns `sha1, count, username, title`, where the `count` is provided by the HIBP input.

