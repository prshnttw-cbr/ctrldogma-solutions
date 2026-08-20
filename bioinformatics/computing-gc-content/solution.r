solve <- function(s) {
  chars <- strsplit(s, "")[[1]]
  gc <- sum(chars == "G" | chars == "C")
  cat(sprintf("%.2f", gc * 100 / nchar(s)))
}

s <- readLines("stdin", n = 1)
solve(s)
