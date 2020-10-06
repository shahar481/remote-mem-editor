# Protocol

## Message structure
All messages have the following structure

```
[4 bytes of length][1 byte message type][message]
```

### Message types

```
01 - Session start
02 - Error
03 - Start command
04 - Command data
```

#### Session start

First the client(the executable) connect to the server(the python).
It sends out a message with all supported commands as so:

```
[4 bytes of length][session start byte][command_id][command_id][command_id][command_id]...
```

Each command is given an id which is one byte in length

#### Error

The error is sent as so:
```
[4 bytes of length][error byte][error message]
```

#### Start command

Comnands are run as so:
```
[4 bytes of length][start command byte][command type byte][command]
```

#### Command Data

This is for data returning from the executable or extra data sent for the command.
Basically any data that is not in the initial start command message.

Structure:
```
[4 bytes of length][command data byte][command type byte][command]
```

### Commands
```
01 - Ps
02 - Attach
03 - Read memory
04 - Write memory
05 - Run shell
```

#### Ps

Will run a process list, command needs no data
```
[4 bytes of length][start command byte][ps type byte]
```
