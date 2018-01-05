# multiAsset

### Requirements
1. System deps
    - python 2.7
    - docker
    - [fabric-samples](https://github.com/hyperledger/fabric-samples.git)
Also see [hyperledger prerequisites](http://hyperledger-fabric.readthedocs.io/en/latest/prereqs.html#prerequisites).

2. Dockerimages
Follow the instruction to [download-platform-specific-binaries](http://hyperledger-fabric.readthedocs.io/en/latest/samples.html#download-platform-specific-binaries).

### Deploy the chaincode
1. Start the network
```bash
cd <fabric-samples>/chaincode-docker-devmode
docker-compose -f docker-compose-simple.yaml up
```
Then wait about 1 minutes to start up.

Check the network via
`docker-compose -f docker-compose-simple.yaml ps`
You will see 4 dockers running.

2. Start the chaincode
Start a new terminal:
```bash
docker exec -it chaincode bash
# you are entering in the `chaincode` docker
cd sacc
go build
CORE_CHAINCODE_ID_NAME=mycc:0 ./sacc
```
Leave it open.

3. Initialize the chaincode
```bash
docker exec -it cli bash
# you are entering in the `cli` docker
peer chaincode install -p chaincodedev/chaincode/sacc -n mycc -v 0
peer chaincode instantiate -n mycc -v 0 -c '{"Args":["a", "10"]}' -C myc
```
Then exit if everything is OK.

### Run the Dapp
```bash
# go to the `multiAsset` dir
./docker_wrapper.sh query '["", "a"]'

# OR just
./main.py
```
You would see the query result.

