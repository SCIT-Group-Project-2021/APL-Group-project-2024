; ModuleID = "/Users/rajae/Desktop/Projects/APL-Group-project-2024/genz-lang/codegen.py"
target triple = "x86_64-apple-darwin23.1.0"
target datalayout = ""

define void @"main"()
{
entry:
  %"i" = alloca i8
  store i8 5, i8* %"i"
  br label %"loop"
loop:
  %".4" = load i8, i8* %"i"
  %"compare_ne" = icmp ne i8 %".4", 0
  br i1 %"compare_ne", label %"body", label %"afterloop"
body:
  %".6" = load i8, i8* %"i"
  %".7" = sub i8 %".6", 1
  store i8 %".7", i8* %"i"
  %".9" = load i8, i8* %"i"
  %".10" = bitcast [5 x i8]* @"fstr-$9433" to i8*
  %".11" = call i32 (i8*, ...) @"printf"(i8* %".10", i8 %".9")
  br label %"loop"
afterloop:
  %".13" = load i8, i8* %"i"
  %".14" = bitcast [5 x i8]* @"fstr-$46548" to i8*
  %".15" = call i32 (i8*, ...) @"printf"(i8* %".14", i8 %".13")
  %".16" = load i8, i8* %"i"
  %".17" = sub i8 %".16", 1
  store i8 %".17", i8* %"i"
  ret void
}

declare i32 @"printf"(i8* %".1", ...)

@"fstr-$9433" = internal constant [5 x i8] c"%i \0a\00"
@"fstr-$46548" = internal constant [5 x i8] c"%i \0a\00"