; ModuleID = "/Users/rajae/Desktop/Projects/APL-Group-project-2024/genz-lang/codegen.py"
target triple = "x86_64-apple-darwin23.1.0"
target datalayout = ""

define void @"main"()
{
entry:
  %".2" = add i8 6, 6
  %".3" = sdiv i8 %".2", 2
  %".4" = bitcast [5 x i8]* @"fstr-$38750" to i8*
  %".5" = call i32 (i8*, ...) @"printf"(i8* %".4", i8 %".3")
  %".6" = mul i8 6, 7
  %".7" = bitcast [5 x i8]* @"fstr-$41283" to i8*
  %".8" = call i32 (i8*, ...) @"printf"(i8* %".7", i8 %".6")
  %".9" = mul i8 7, 8
  %".10" = bitcast [5 x i8]* @"fstr-$82875" to i8*
  %".11" = call i32 (i8*, ...) @"printf"(i8* %".10", i8 %".9")
  ret void
}

declare i32 @"printf"(i8* %".1", ...)

@"fstr-$38750" = internal constant [5 x i8] c"%i \0a\00"
@"fstr-$41283" = internal constant [5 x i8] c"%i \0a\00"
@"fstr-$82875" = internal constant [5 x i8] c"%i \0a\00"