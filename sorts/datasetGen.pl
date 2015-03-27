#!/usr/bin/perl

# Perl Script for generating comma delineated integers lists
# Ideally pipe the output into a text file or directly into another program
# Pass number of integers as command line standard-input argument
# By Marshall Ehlinger

use strict;
use warnings;

my $NUM_VALS = $ARGV[0];

for (my $i = 0; $i < $NUM_VALS; $i++) {
	print(int(rand(100)));
	print(",");
}