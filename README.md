# What is this?

This is a small python script to generate hcmask masks for dotted decimal IPv4 addresses.

## Masks

A mask is a pattern for hashcat or John the Ripper.
?d is a predefined charset refering to a digit between 0 and 9.
Both hashcat and Jonh the Ripper also support custom charsets.

For instance an IPv4 address might look like this:

```
192.168.0.54
```

A mask pattern for this could be:

```
?d?d?d.?d?d?d.?d.?d?d
```

But since a dotted decimal number can only be between 0 and 255
three digit dotted decimal numbers will always begins with 1 or 2.
So the mask can be optimized using a custom charset containing only
the digits 1 and 2.

In cmdline hashcat this is written as:

```
hashcat ... -a 3 -1 12 ?1?d?d.?1?d?d.?d.?d?d
```

(-a 3 is for mask attack)

```
john ... -1:12 -mask:?1?d?d.?1?d?d.?d.?d
```

... means other flags, like hash format and hash file.

## hcmask

Hcmask is a hashcat special format for putting many masks into one file. The custom
charset syntax then becomes:

```
12,?1?d?d.?1?d?d.?d.?d?d
```

*gen_ipaddr_hcmask.py* generates all *81* possible masks for dotted decimal IPv4
addresses in hcmask format.


```Shell
$ hashcat -O -m 1700 --potfile-path=hc.pot router.sha512 -a 3 ipaddr.hcmask
```

```Shell
$ hashcat -O -m 0 --potfile-path=hc.pot router.md5 -a 3 ipaddr.hcmask
```

## TODO

IPv4 can also be written in short notation, leaving out 0. This is not currently supported.
Example:

* 192.168.1 -> 192.168.0.1
* 10.1 -> 10.0.0.1
