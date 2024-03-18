; ModuleID = "/Users/rajae/Desktop/Projects/APL-Group-project-2024/genz-lang/codegen.py"
target triple = "x86_64-apple-darwin23.1.0"
target datalayout = ""

define void @"main"()
{
entry:
  %"compare_ge" = icmp sge i8 23, 18
  br i1 %"compare_ge", label %"entry.if", label %"entry.else"
entry.if:
  %".3" = bitcast [5 x i8]* @"fstr-$12761" to i8*
  %".4" = call i32 (i8*, ...) @"printf"(i8* %".3", i8 1)
  br label %"entry.endif"
entry.else:
  %".6" = bitcast [5 x i8]* @"fstr-$86052" to i8*
  %".7" = call i32 (i8*, ...) @"printf"(i8* %".6", i8 0)
  br label %"entry.endif"
entry.endif:
  ret void
}

declare i32 @"printf"(i8* %".1", ...)

@"fstr-$12761" = internal constant [5 x i8] c"%i \0a\00"
@"fstr-$86052" = internal constant [5 x i8] c"%i \0a\00"