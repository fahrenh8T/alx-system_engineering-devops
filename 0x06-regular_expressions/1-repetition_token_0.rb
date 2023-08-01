#!/usr/bin/env ruby
# script takes the first command-line arg, scans it for occurrences of the regular expression.
puts ARGV[0].scan(/hbt{2,5}n/).join
