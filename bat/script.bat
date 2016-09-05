@echo off
setlocal

REM set _output=output.txt

:parse_options
if not "%1" == "" (
    if "%1" == "-?" (
       goto :usage
    )
    REM if "%1" == "-o" (
    REM     set _output=%2
    REM     shift
    REM )
    shift
    goto :parse_options
)

REM TODO: implement

goto :eof

:usage
echo.
REM TODO: describe usage
REM echo %~nx0 [OPTIONS]
REM echo OPTIONS:
REM echo     -o OUTPUT_PATH  path to output file ^(default: %_output%^)
echo.
goto :eof

endlocal