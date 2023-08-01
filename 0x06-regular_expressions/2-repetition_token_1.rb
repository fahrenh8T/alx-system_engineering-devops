#!/usr/bin/env ruby
# script takes the 1st command line arg, scans it for occurrences of the regular expression.
puts ARGV[0].scan(/hb?t?n/).join