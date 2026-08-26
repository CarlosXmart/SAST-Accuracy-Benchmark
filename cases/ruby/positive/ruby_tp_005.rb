require 'digest'
def ruby_tp_005(data)
  # XG-BENCH:RUBY-TP-005 START
  Digest::MD5.hexdigest(data)
  # XG-BENCH:RUBY-TP-005 END
end
