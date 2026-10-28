$ErrorActionPreference = "Stop"

$output = Join-Path $PSScriptRoot "..\data\windows_cng.bin"
$output = [System.IO.Path]::GetFullPath($output)

$bytes = New-Object byte[] 1048576
$rng = [System.Security.Cryptography.RandomNumberGenerator]::Create()

try {
    $rng.GetBytes($bytes)
    [System.IO.File]::WriteAllBytes($output, $bytes)
}
finally {
    $rng.Dispose()
}

Write-Host "Windows cryptographic random data generated."
Write-Host "Output: $output"
Write-Host "Bytes: $((Get-Item $output).Length)"