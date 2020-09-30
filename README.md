# Protocol
This is how a "Session" goes:
* First the binary tries to connect to the python

* Then it sends out the process list like this:

```
[4 byte length of pid][pid in char]
```
```
[4 byte length of cmdline][cmdline]
```
Until a message is sent with an empty pid so like this:
```
00 00 00 00
```

* Then the client has 2 options, either send the letter 'r'
which will send the ps again
or you can send the pid which will select that process and attach to it

This is how you send r to repeat the process list 
```
[4 byte length of r]r
```

This is how you attach to a pid
```
[4 byte length of pid][pid in char]
```

It will reply with an error message
```
[4 byte length of error message][error message]
```
If it comes as 0 length then there was no error

### Process attached
* Now it sends you the /proc/pid/maps as so:
```
[4 byte length of map entry][map entry]
```

Until an empty message comes
```
00 00 00 00 
```

* Now you can send either 'r' to repeat the proc maps or send 'i' to get memory dumps of given addresses
or 'w' to write to specific addresses

It will reply with an error message
```
[4 byte length of error message][error message]
```
If it comes as 0 length then there was no error


### Reading
```
[4 byte length of i]i
``` 

It will reply with an error message
```
[4 byte length of error message][error message]
```
If it comes as 0 length then there was no error

then you give it an address and length and it will read the buffer and send it back
```
[4 byte length of start address]address
```

```
[4 byte length of read length]length
```

It will reply with an error message
```
[4 byte length of error message][error message]
```

```
[4 byte length of buffer][memory buffer]
```