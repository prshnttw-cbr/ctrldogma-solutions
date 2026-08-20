lines <- readLines(file("stdin"))
ident <- NULL
buf <- character(0)
idents <- character(0)
lens <- integer(0)
for (line in lines) {
  line <- trimws(line)
  if (nchar(line) == 0) next
  if (startsWith(line, ">")) {
    if (!is.null(ident)) {
      idents <- c(idents, ident)
      lens <- c(lens, nchar(paste(buf, collapse = "")))
    }
    header <- substring(line, 2)
    if (nchar(header) > 0) {
      parts <- strsplit(header, "\\s+")[[1]]
      ident <- parts[1]
    } else {
      ident <- ""
    }
    buf <- character(0)
  } else {
    buf <- c(buf, line)
  }
}
if (!is.null(ident)) {
  idents <- c(idents, ident)
  lens <- c(lens, nchar(paste(buf, collapse = "")))
}
for (i in seq_along(idents)) {
  cat(idents[i], " ", lens[i], "\n", sep = "")
}
