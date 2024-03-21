; ModuleID = "/Users/rajae/Desktop/Projects/APL-Group-project-2024/genz-lang/codegen.py"
target triple = "x86_64-apple-darwin23.1.0"
target datalayout = ""

define void @"main"()
{
entry:
  %"age" = alloca i8
  store i8 21, i8* %"age"
  %".3" = load i8, i8* %"age"
  %"compare_ge" = icmp sge i8 %".3", 18
  br i1 %"compare_ge", label %"entry.if", label %"entry.else"
entry.if:
  %".5" = bitcast [5 x i8]* @"fstr-$38576" to i8*
  %".6" = call i32 (i8*, ...) @"printf"(i8* %".5", i8 1)
  br label %"entry.endif"
entry.else:
  %".8" = bitcast [5 x i8]* @"fstr-$19821" to i8*
  %".9" = call i32 (i8*, ...) @"printf"(i8* %".8", i8 0)
  br label %"entry.endif"
entry.endif:
  ret void
}

declare i32 @"printf"(i8* %".1", ...)

@"fstr-$38576" = internal constant [5 x i8] c"%i \0a\00"
@"fstr-$19821" = internal constant [5 x i8] c"%i \0a\00"