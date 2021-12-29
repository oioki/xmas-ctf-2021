# Day 19. Santa's library

> Santa found this library on his computer. Can you help him figure out what it does?

[SantasLibrary.zip](./SantasLibrary.zip)

## Solution

This time, we have a .NET DLL file (dynamic library), and again, we can use [dnSpy](https://github.com/dnSpy/dnSpy/releases) to decompile it. I saved the source code for `Main()` and `Func2()` functions to [source.cs](./source.cs). Also I have converted it to class because I did not know how to invoke functions from the DLL.

If you inspect the source code briefly, you will notice two sequences of bytes - one in `Main()`, another in `Func2()`. They are combined somehow in the second function, together with some randomness, XOR (`ExclusiveOr`), and IL-representation of the Func2 function itself (note `GetILAsByteArray`). But it's hard to follow manually what's going on, so we need to debug it somehow.

I struggled to setup a full-blown .NET work environment, so I used an online tool - [.NET Fiddle](https://dotnetfiddle.net/). It allows you to execute .NET code and play with it right in the browser. Note you need to select `.NET 6` compiler for this.

Unfortunately, if you try to run the code, you will see the error:

```
Unhandled exception. System.ArgumentException: Expression of type 'System.Int32' cannot be used for assignment to type 'System.Random'  
 at System.Linq.Expressions.Expression.Assign(Expression left, Expression right)  
 at Program.Func2(Byte[] bytes)  
 at Program.Main(String[] args)  
Command terminated by signal 6
```

and the offending line was:

```
        Expression.Assign(parameterExpression5, Expression.New(typeof(int))),
```

Apparently, challenge creator encrypted the flag with the abovementioned arrays, then messed up the source code, so we have to fix it. For our error, the fix was:

```
        //Expression.Assign(parameterExpression5, Expression.New(typeof(int))),
        Expression.Assign(parameterExpression5, Expression.New(typeof(Random))),
```

Now, we have another error:

```
Unhandled exception. System.ArgumentException: Argument types do not match  
 at System.Linq.Expressions.Expression.Constant(Object value, Type type)  
 at Program.Func2(Byte[] bytes)  
 at Program.Main(String[] args)  
Command terminated by signal 6
```

and the offending line was:

```
        Expression.Assign(parameterExpression4, Expression.Constant(0, typeof(byte))),
```

The fix is similar:

```
        //Expression.Assign(parameterExpression4, Expression.Constant(0, typeof(byte))),
        Expression.Assign(parameterExpression4, Expression.Constant(0, typeof(int))),
```

Just in case, see the [modified](./modified.cs) source code.

Now, when you run the program, you will get:

```
ctf{4rthurFChr1stma5}
```

The flag is almost complete! I did not try to fix the original program, but just guessed the correct flag which was one symbol off:

```
ctf{4rthur_Chr1stma5}
```
