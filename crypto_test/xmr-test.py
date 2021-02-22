from moneropy import account

# seed, sk, vk, addr = account.gen_new_wallet()
#
# address = addr
# privateKey = sk

sk, vk, addr = account.account_from_spend_key(sk='e22b4f6e0d81cd7b71f5d2bcf4191c8ed893c0adac59c9f2bf22c27cece1f90d')

address = addr
# privateKey = sk

print(address)
# print(privateKey)

# 476vPMXFMjJKMrzTtBDCtfNYxVbX1HnqxTaYmoJ8sz9oZLFAbKastHXMVX5BckcdK9fawU4NgooPsYjWngfKFrq4FLMRNiU
# e22b4f6e0d81cd7b71f5d2bcf4191c8ed893c0adac59c9f2bf22c27cece1f90d