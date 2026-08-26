require 'digest'
def ruby_tn_005(data)
  # XG-BENCH:RUBY-TN-005 START
  Digest::SHA256.hexdigest(data)
  # XG-BENCH:RUBY-TN-005 END
end
