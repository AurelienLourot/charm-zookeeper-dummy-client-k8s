# Publishing the charm to [the store](https://charmhub.io/zookeeper-dummy-client-k8s)

```bash
$ charmcraft pack
$ charmcraft login
$ charmcraft upload zookeeper-dummy-client-k8s.charm
Revision 3 of 'zookeeper-dummy-client-k8s' created
$ git tag rev003
$ git push --tags
$ charmcraft release zookeeper-dummy-client-k8s --revision=3 --channel=stable --resource=ubuntu-image:1
$ charmcraft status zookeeper-dummy-client-k8s
Track    Channel    Version    Revision    Resources
latest   stable     3          3           ubuntu-image (r1)
         candidate  ↑          ↑           ↑
         beta       ↑          ↑           ↑
         edge       ↑          ↑           ↑
```

> **NOTE**: the `ubuntu-image:1` resource has already been created with
>
> ```bash
> $ charmcraft upload-resource --image ubuntu zookeeper-dummy-client-k8s ubuntu-image
> Revision 1 created of resource 'ubuntu-image' for charm 'zookeeper-dummy-client-k8s'
> ```

See the
[Charmed Operator Framework documentation](https://juju.is/docs/sdk/publishing)
for more details.
