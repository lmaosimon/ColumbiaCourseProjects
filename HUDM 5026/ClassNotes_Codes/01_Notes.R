### The c() function is used to create vectors.
c(1,3,5,7,9)
c(-12.3, 13, 2, 6, 34)
c(1,2,3)*3

### Can also create character vectors by using quotes.
c("a", "b", "c")
### Single quote works as well.
c('a', 'b', 'c')
### Can't do arithmetic with characters.
3 + c("a", "b")
### Logical vectors are possible as well. 
c(TRUE, FALSE, TRUE, TRUE)
### If you force arithmetic on a logical, it will
### coerce TRUE to 1 and FALSE to 0.
4*c(TRUE, FALSE, TRUE)

### seq() is a function that creates a vector based on a sequence.
seq(from = 1, to = 10, by = 1)
seq(from = 10, to = 0, by = -5)
seq(from = 10, to = 0, by = 5) # error: incorrect sign
seq() # default from = to = by = 1
### The colon ':' is a shortcut for seq with by = 1 or by = -1.
1:10
10:1
v1 <- 1:10 # creates a vector of mode numeric, type integer
v2 <- -2.5:5.5 # creates a vector of mode numeric, type double

### rep() is a function that creates a vector by repeating an argument.
rep(x = c(1, 3, 5, 7, 9), times = 5, each = 1)
rep(x = c(1, 3, 5, 7, 9), times = 1, each = 5)
rep(x = c(1, 2, 3), times = 5, each = 1)
rep(x = c(1, 2, 3), times = 1, each = 5)
rep(x = c(1, 2, 3), times = 5, each = 5)

### The assign() function may be used to assign a value to a name.
assign(x = "dd", value = 10)
dd
assign(x = "vec1", value = 1:4)
vec1

### The assignment arrow, <-, is a shortcut. That is, vec2 <- c(4, 2, 3, 2, 1)
### is the same as assign(x = "vec2", value = c(4, 2, 3, 2, 1))
vec2 <- c(4, 2, 3, 2, 1)
vec2
sc1 <- -500
sc1

