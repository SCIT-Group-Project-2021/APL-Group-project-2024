; ModuleID = "/Users/rajae/Desktop/Projects/APL-Group-project-2024/genz-lang/codegen.py"
target triple = "x86_64-apple-darwin23.1.0"
target datalayout = ""

define void @"main"()
{
entry:
  %"compare_eq" = icmp eq i8 1, 1
  %".2" = bitcast [5 x i8]* @"fstr-$30134" to i8*
  %".3" = call i32 (i8*, ...) @"printf"(i8* %".2", i1 %"compare_eq")
  %"compare_ne" = icmp ne i8 1, 1
  %".4" = bitcast [5 x i8]* @"fstr-$29689" to i8*
  %".5" = call i32 (i8*, ...) @"printf"(i8* %".4", i1 %"compare_ne")
  %"compare_gt" = icmp sgt i8 2, 3
  %".6" = bitcast [5 x i8]* @"fstr-$91453" to i8*
  %".7" = call i32 (i8*, ...) @"printf"(i8* %".6", i1 %"compare_gt")
  %"compare_lt" = icmp slt i8 5, 10
  %".8" = bitcast [5 x i8]* @"fstr-$23925" to i8*
  %".9" = call i32 (i8*, ...) @"printf"(i8* %".8", i1 %"compare_lt")
  %"compare_ge" = icmp sge i8 21, 18
  %".10" = bitcast [5 x i8]* @"fstr-$98831" to i8*
  %".11" = call i32 (i8*, ...) @"printf"(i8* %".10", i1 %"compare_ge")
  %"compare_le" = icmp sle i8 21, 18
  %".12" = bitcast [5 x i8]* @"fstr-$17454" to i8*
  %".13" = call i32 (i8*, ...) @"printf"(i8* %".12", i1 %"compare_le")
  ret void
}

declare i32 @"printf"(i8* %".1", ...)

@"fstr-$30134" = internal constant [5 x i8] c"%i \0a\00"
@"fstr-$29689" = internal constant [5 x i8] c"%i \0a\00"
@"fstr-$91453" = internal constant [5 x i8] c"%i \0a\00"
@"fstr-$23925" = internal constant [5 x i8] c"%i \0a\00"
@"fstr-$98831" = internal constant [5 x i8] c"%i \0a\00"
@"fstr-$17454" = internal constant [5 x i8] c"%i \0a\00"