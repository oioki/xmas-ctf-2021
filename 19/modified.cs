using System;
using System.Linq.Expressions;
using System.Collections.Generic;
using System.Text;


public class Program
{

    // App1.Program
// Token: 0x06000001 RID: 1 RVA: 0x00002050 File Offset: 0x00000250
public static void Main(string[] args)
{
    byte[] bytes = new byte[]
    {
        86,
        26,
        42,
        155,
        110,
        19,
        66,
        3,
        100,
        29,
        124,
        117,
        84,
        61,
        75,
        19,
        11,
        181,
        89,
        123,
        48
    };
    Program.Func2(bytes);
}

    // App1.Program
// Token: 0x06000002 RID: 2 RVA: 0x00002078 File Offset: 0x00000278
public static void Func2(byte[] bytes)
{
    LabelTarget labelTarget = Expression.Label(typeof(byte[]));
    LabelTarget labelTarget2 = Expression.Label();
    LabelTarget labelTarget3 = Expression.Label();
    ParameterExpression parameterExpression = Expression.Variable(typeof(byte[]));
    ParameterExpression parameterExpression2 = Expression.Variable(typeof(byte[]));
    ParameterExpression parameterExpression3 = Expression.Variable(typeof(byte[]));
    ParameterExpression parameterExpression4 = Expression.Variable(typeof(int));
    ParameterExpression parameterExpression5 = Expression.Variable(typeof(Random));
    ParameterExpression parameterExpression6 = Expression.Variable(typeof(int));
    Expression body = Expression.Block(new ParameterExpression[]
    {
        parameterExpression,
        parameterExpression2,
        parameterExpression3,
        parameterExpression4,
        parameterExpression5,
        parameterExpression6
    }, new Expression[]
    {
        Expression.Assign(parameterExpression, Expression.Constant(bytes)),
        Expression.Assign(parameterExpression2, Expression.Constant(new byte[]
        {
            98,
            48,
            122,
            53,
            53,
            117,
            98,
            115,
            56,
            52,
            71,
            71,
            83,
            49,
            102,
            120,
            53,
            54,
            66,
            67,
            120,
            97,
            57,
            102,
            106,
            72,
            97,
            111,
            108,
            122,
            54,
            66,
            53,
            83,
            112,
            114,
            113,
            101,
            84,
            100,
            102,
            107,
            65,
            118,
            110,
            116,
            53,
            84,
            81,
            76,
            76,
            108,
            90,
            67,
            103,
            54,
            98,
            52,
            71,
            73,
            49,
            112,
            61,
            61
        })),
        Expression.Assign(parameterExpression3, Expression.Call(Expression.Call(Expression.Call(Expression.Constant(typeof(Program), typeof(Type)), "GetMethod", null, new Expression[]
        {
            Expression.Constant("Func2")
        }), "GetMethodBody", null, Array.Empty<Expression>()), "GetILAsByteArray", null, Array.Empty<Expression>())),
        Expression.Assign(parameterExpression5, Expression.New(typeof(Random).GetConstructor(new Type[]
        {
            typeof(int)
        }), new Expression[]
        {
            Expression.Constant(83428)
        })),
        //Expression.Assign(parameterExpression5, Expression.New(typeof(int))),
        Expression.Assign(parameterExpression5, Expression.New(typeof(Random))),
        //Expression.Assign(parameterExpression4, Expression.Constant(0, typeof(byte))),
        Expression.Assign(parameterExpression4, Expression.Constant(0, typeof(int))),
        Expression.Assign(parameterExpression6, Expression.Constant(0)),
        Expression.Loop(Expression.IfThenElse(Expression.LessThan(parameterExpression4, Expression.Property(parameterExpression3, "Length")), Expression.Block(Expression.Assign(parameterExpression6, Expression.Add(parameterExpression6, Expression.Convert(Expression.ArrayAccess(parameterExpression3, new Expression[]
        {
            parameterExpression4
        }), typeof(int)))), Expression.Assign(parameterExpression4, Expression.Add(parameterExpression4, Expression.Constant(2)))), Expression.Break(labelTarget3, parameterExpression)), labelTarget3),
        Expression.Assign(parameterExpression4, Expression.Constant(0)),
        Expression.Loop(Expression.IfThenElse(Expression.LessThan(parameterExpression4, Expression.Property(parameterExpression2, "Length")), Expression.Block(Expression.Assign(Expression.ArrayAccess(parameterExpression2, new Expression[]
        {
            parameterExpression4
        }), Expression.MakeBinary(ExpressionType.ExclusiveOr, Expression.ArrayAccess(parameterExpression2, new Expression[]
        {
            parameterExpression4
        }), Expression.ArrayAccess(parameterExpression3, new Expression[]
        {
            Expression.Block(new Expression[]
            {
                Expression.Call(Expression.New(typeof(Random).GetConstructor(new Type[]
                {
                    typeof(int)
                }), new Expression[]
                {
                    parameterExpression4
                }), "Next", null, new Expression[]
                {
                    Expression.Constant(380),
                    Expression.Constant(450)
                })
            })
        }))), Expression.PostIncrementAssign(parameterExpression4)), Expression.Break(labelTarget2)), labelTarget2),
        Expression.Assign(parameterExpression4, Expression.Constant(0)),
        Expression.Loop(Expression.IfThenElse(Expression.LessThan(parameterExpression4, Expression.Property(parameterExpression, "Length")), Expression.Block(Expression.Assign(Expression.ArrayAccess(parameterExpression, new Expression[]
        {
            parameterExpression4
        }), Expression.MakeBinary(ExpressionType.ExclusiveOr, Expression.ArrayAccess(parameterExpression, new Expression[]
        {
            parameterExpression4
        }), Expression.ArrayAccess(parameterExpression2, new Expression[]
        {
            Expression.Block(new Expression[]
            {
                Expression.Call(Expression.New(typeof(Random).GetConstructor(new Type[]
                {
                    typeof(int)
                }), new Expression[]
                {
                    parameterExpression4
                }), "Next", null, new Expression[]
                {
                    Expression.Constant(0),
                    Expression.Property(parameterExpression2, "Length")
                })
            })
        }))), Expression.PostIncrementAssign(parameterExpression4)), Expression.Break(labelTarget, parameterExpression)), labelTarget)
    });
    Func<byte[]> func = Expression.Lambda<Func<byte[]>>(body, Array.Empty<ParameterExpression>()).Compile();
    byte[] bytes2 = func();
    Console.WriteLine(Encoding.UTF8.GetString(bytes2));
}

}
