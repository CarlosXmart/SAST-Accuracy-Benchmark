def ruby_tn_003(name)
  # XG-BENCH:RUBY-TN-003 START
  base = File.expand_path('/srv/data')
  target = File.expand_path(name, base)
  raise 'outside base' unless target == base || target.start_with?(base + File::SEPARATOR)
  File.read(target)
  # XG-BENCH:RUBY-TN-003 END
end
