# (Wklej treść, CTRL+O, Enter, CTRL+X)

ssh-keygen -Y sign -n aura-governance -f ~/.ssh/id_ed25519 AUTHORITY_BINDING_RECORD.md
git add AUTHORITY_BINDING_RECORD.md AUTHORITY_BINDING_RECORD.md.sig
git commit -S -m "Ratify Root Identity and Authority Binding (AURA-BIND-ROOT-v1.0)"
git push origin main
# AURA AUTHORITY AND IDENTITY BINDING RECORD
Artifact_ID: AURA-BIND-ROOT-v1.0
Status: RATIFIED

Signer_Identity:
  Full_Name: Kamil Krasiński
  Email: kontakt.vaidt@gmail.com
  GitHub_Accounts:
    - vaidt
    - Kamil1230xd
    - Aura-IDToken

Cryptographic_Root:
  Key_Type: ssh-ed25519
  Fingerprint: SHA256:u9HaNYWZGQYvGET5ZaX2c/V56MzL0Xo7Ilg9M1pZRwU
  Public_Key: ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIPtUzzZnVuXqd+HixKurmhIELs1RGO6He1nS/dOY80X4 genesis-aura

Attestation:
  I hereby attest that the SSH key with fingerprint SHA256:u9HaNYWZGQYvGET5ZaX2c/V56MzL0Xo7Ilg9M1pZRwU is under my exclusive physical possession and control. This key is irrevocably bound to my persona as the Original Creator and Protocol Custodian of the AURA architecture. All decrees signed with this key in namespaces 'aura-genesis' and 'aura-governance' carry full constitutive and protocol authority.

