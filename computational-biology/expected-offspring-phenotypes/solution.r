counts <- as.numeric(strsplit(trimws(readLines(file("stdin"), n = 1)), "\\s+")[[1]])
probs <- c(1.0, 1.0, 1.0, 0.75, 0.5, 0.0)
result <- sum(counts * 2 * probs)
cat(sprintf("%.5f", result), "\n", sep = "")
