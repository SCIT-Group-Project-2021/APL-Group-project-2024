; ModuleID = "/Users/rajae/Desktop/Projects/APL-Group-project-2024/genz-lang/codegen.py"
target triple = "x86_64-apple-darwin23.1.0"
target datalayout = ""

define void @"main"()
{
entry:
  %".2" = mul i8 2, 2
  %".3" = sdiv i8 4, %".2"
  %".4" = mul i8 %".3", 2
  %".5" = bitcast [5 x i8]* @"fstr" to i8*
  %".6" = call i32 (i8*, ...) @"printf"(i8* %".5", i8 %".4")
  ret void
}

declare i32 @"printf"(i8* %".1", ...)

@"fstr" = internal constant [5 x i8] c"%i \0a\00"