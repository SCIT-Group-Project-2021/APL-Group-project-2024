; ModuleID = "G:\Programming\Projects\APL-Group-project-2024\genz-lang\codegen.py"
target triple = "x86_64-pc-windows-msvc"
target datalayout = ""

define void @"main"()
{
entry:
  %"compare_eq" = icmp eq i8 1, 1
  %".2" = bitcast [5 x i8]* @"fstr-$77863" to i8*
  %".3" = call i32 (i8*, ...) @"printf"(i8* %".2", i1 %"compare_eq")
  %"compare_ne" = icmp ne i8 1, 1
  %".4" = bitcast [5 x i8]* @"fstr-$96945" to i8*
  %".5" = call i32 (i8*, ...) @"printf"(i8* %".4", i1 %"compare_ne")
  %"compare_gt" = icmp sgt i8 2, 3
  %".6" = bitcast [5 x i8]* @"fstr-$20137" to i8*
  %".7" = call i32 (i8*, ...) @"printf"(i8* %".6", i1 %"compare_gt")
  %"compare_lt" = icmp slt i8 5, 10
  %".8" = bitcast [5 x i8]* @"fstr-$65877" to i8*
  %".9" = call i32 (i8*, ...) @"printf"(i8* %".8", i1 %"compare_lt")
  %"compare_ge" = icmp sge i8 21, 18
  %".10" = bitcast [5 x i8]* @"fstr-$49327" to i8*
  %".11" = call i32 (i8*, ...) @"printf"(i8* %".10", i1 %"compare_ge")
  %"compare_le" = icmp sle i8 21, 18
  %".12" = bitcast [5 x i8]* @"fstr-$93329" to i8*
  %".13" = call i32 (i8*, ...) @"printf"(i8* %".12", i1 %"compare_le")
  ret void
}

declare i32 @"printf"(i8* %".1", ...)

@"fstr-$77863" = internal constant [5 x i8] c"%i \0a\00"
@"fstr-$96945" = internal constant [5 x i8] c"%i \0a\00"
@"fstr-$20137" = internal constant [5 x i8] c"%i \0a\00"
@"fstr-$65877" = internal constant [5 x i8] c"%i \0a\00"
@"fstr-$49327" = internal constant [5 x i8] c"%i \0a\00"
@"fstr-$93329" = internal constant [5 x i8] c"%i \0a\00"