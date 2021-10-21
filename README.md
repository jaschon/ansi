# Ansi
ANSI Terminal Functions


## Example

```
c = Ansi()
```

## Move Cursor

```
c.up(<num of lines. default 1>)
c.down(<num of lines. default 1>)
c.left(<num of lines. default 1>)
c.right(<num of lines. default 1>)

c.row(<num of rows. default 0>)
c.col(<num of cols. default 0>)

c.goto(<row>, <col>)

c.pg_up(<num of rows. default 0>)
c.pg_down(<num of cols. default 0>)
```

## Clear Screen

```
c.clear()

#clear end of line
c.cleareol() 

#clear beginning of line
c.clearbol()

#clear col to the end
c.clearln(<num of cols to end. default 2>)

```

## Show/Hide Cursor

```
c.show()
c.hide()
```

## Save/Resore Cursor POS

```
c.save()
c.restore()
```

## Basic Color

```
c.color(<color number>)
c.style(<style number>)
c.background(<color number>)
```

## Reset Screen
  
```
c.reset()
```
