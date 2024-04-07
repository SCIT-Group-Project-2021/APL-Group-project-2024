; ModuleID = "C:\Users\jazmi\VS Code Projects\APL2024\APL-Group-project-2024\genz-lang\codegen.py"
target triple = "x86_64-pc-windows-msvc"
target datalayout = ""

define void @"main"()
{
entry:
  %"age" = alloca i8
  store i8 21, i8* %"age"
  %"isMale" = alloca i1
  store i1 1, i1* %"isMale"
  %".4" = load i8, i8* %"age"
  %"compare_ge" = icmp sge i8 %".4", 18
  %".5" = load i1, i1* %"isMale"
  %".6" = and i1 %"compare_ge", %".5"
  br i1 %".6", label %"entry.if", label %"entry.else"
entry.if:
  %".8" = bitcast [5 x i8]* @"fstr-$8949" to i8*
  %".9" = call i32 (i8*, ...) @"printf"(i8* %".8", i1 1)
  br label %"entry.endif"
entry.else:
  %".11" = bitcast [5 x i8]* @"fstr-$87596" to i8*
  %".12" = call i32 (i8*, ...) @"printf"(i8* %".11", i1 0)
  br label %"entry.endif"
entry.endif:
  ret void
}

declare i32 @"printf"(i8* %".1", ...)

@"fstr-$8949" = internal constant [5 x i8] c"%i \0a\00"
@"fstr-$87596" = internal constant [5 x i8] c"%i \0a\00"