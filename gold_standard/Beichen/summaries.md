# Gold Standard Summaries
"The Multi-tiered Future of Storage: Understanding Cost and Performance Trade-offs in Modern Storage Systems"
#### NOTE
First chapter is summarized by me. The last 3 chapters are based on 3 papers, so I grabbed the abstract of each paper as summary. It looks like the chapter 2 is an unpublished paper, but still it gave us a summary in chapter 2.4

### Chapter 1
In the last decade, the landscape of storage hardware and software has
changed considerably. On the hardware side, hard disk drives and DRAM
devices have been supplanted by fast, reliable solid-state drives
(SSDs).
Persistent memory devices are making their way into the market. These
new hardware devices have challenged the assumptions inherent in the
design of traditional storage systems, presented a new set of
challenges such as asynchronous read/write latencies and relatively low
endurance. On the software sides, there are two major trends the rise
of cloud-based storage services and new application workloads.

### Chapter 2
thmCache, a tiered cache design that conserves the lifetime of low-endurance persistent memory devices such as PCM by combining them with high- endurance PMEM devices. thmCache achieves this by caching write-intensive blocks in the high-endurance tier in order to absorb as many writes as possible. This way, our approach reduces the write traffic to the low-endurance tier. We extended the AccuSim cache simulator to support a hybrid PMEM architecture and implemented thmCache in it. Our evaluation shows that for write-intensive workloads, thmCache can achieve on average 75% reduction in PCM write traffic using DRAM of size 15% that of the PCM size, while maintaining a hit ratio that is over 99% of that achieved using a non-tiered, PCM-only, ARC-based cache. Thus, our approach offers a practical solution for realizing tiered caching systems for overcoming the drawbacks of persistent memory devices.

### Chapter 3
Cast, a Cloud Analytics Storage
Tiering solution that cloud tenants can use to reduce monetary
cost and improve performance of analytics workloads.
The approach takes the first step towards providing storage
tiering support for data analytics in the cloud. Cast
performs offline workload profiling to construct job performance
prediction models on different cloud storage services,
and combines these models with workload specifications and
high-level tenant goals to generate a cost-effective data placement
and storage provisioning plan. Furthermore, we build
Cast++ to enhance Cast’s optimization model by incorporating
data reuse patterns and across-jobs interdependencies
common in realistic analytics workloads. Tests with production
workload traces from Facebook and a 400-core Google
Cloud based Hadoop cluster demonstrate that Cast++ achieves
1.21× performance and reduces deployment costs by 51.4%
compared to local storage configuration.

### Chapter 4
Cloud object stores are increasingly becoming the de
facto storage choice for big data analytics platforms,
mainly because they simplify the management of large
blocks of data at scale. To ensure cost-effectiveness of
the storage service, the object stores use hard disk drives
(HDDs). However, the lower performance of HDDs affect
tenants who have strict performance requirements
for their big data applications. The use of faster storage
devices such as solid state drives (SSDs) is thus desirable
by the tenants, but incurs significant maintenance
costs to the provider. We design a tiered object store for
the cloud, which comprises both fast and slow storage
devices. The resulting hybrid store exposes the tiering
to tenants with a dynamic pricing model that is based on
the tenants’ usage and the provider’s desire to maximize
profits. The tenants leverage knowledge of their workloads
and current pricing information to select a data
placement strategy that would meet the application requirements
at the lowest cost. Our approach allows both
a service provider and its tenants to engage in a pricing
game, which our results show yields a win–win situation.
