# Remote Memory Editor
This project is for editing parts of memory for debugging/researching remotely.

Mainly for debugging on very old/hard to use systems where working on them is not an option.

It has two key components, executable which is the C code and python which controls the executable.

## Usage

### Python

Use ipython for this to be much easier to use

```
import mem_editor
```

Then create a server object as so:
```
s = mem_editor.server(LISTEN_IP, LISTEN_PORT)
```

And make it start listening
```
s.wait_for_connection()
```

Next you can use the following commands:

#### Commands

##### Process list

Use 
```
s.ps()
```

This will return an array with
```
(PID,Process name)
```

##### Attach

Use
```
s.attach(PID)
```

This will return an error code, 0 if it succeeded

##### Show procmaps

Use 
```
s.proc_maps()
```

This will return an array with a ProcMapEntry object

##### Read memory

Use
```
s.read_mem(PID, START_ADDRESS, LENGTH)
```
This will read /proc/PID/mem in the given address.
May need to attach for it to work on older kernels.

This will return a MemoryChunk object

