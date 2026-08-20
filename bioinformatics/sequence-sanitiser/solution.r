s <- trimws(readLines(file("stdin"), n = 1))
chars <- strsplit(toupper(s), "")[[1]]
clean_chars <- chars[chars %in% c("A", "C", "G", "T")]
clean <- paste(clean_chars, collapse = "")
cat(clean, "\n", sep = "")
cat(nchar(s) - length(clean_chars), "\n", sep = "")
