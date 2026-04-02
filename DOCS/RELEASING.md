# Releasing

Use lightweight tagged releases for teammate distribution.

## Release Flow

1. Ensure tests pass locally.
2. Commit the intended release state.
3. Create an annotated version tag.
4. Push the branch and tag.
5. Ask teammates to run `./update.sh`.

## Example

```bash
git tag -a v0.1.0 -m "AirTable PBGL v0.1.0"
git push origin main --tags
```

## Notes

- `setup.sh` is for first-time installation.
- `update.sh` is for existing installs.
- Keep committed schema markdown current when Airtable metadata changes.
