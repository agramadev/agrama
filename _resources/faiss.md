├── .github
    └── ISSUE_TEMPLATE.md
├── CHANGELOG.md
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── INSTALL.md
├── README.md
├── benchs
    ├── README.md
    ├── bench_all_ivf
    │   └── README.md
    ├── distributed_ondisk
    │   └── README.md
    └── link_and_code
    │   └── README.md
├── c_api
    └── INSTALL.md
├── contrib
    ├── README.md
    └── torch
    │   └── README.md
└── demos
    ├── README.md
    ├── offline_ivf
        └── README.md
    └── rocksdb_ivf
        └── README.md


/.github/ISSUE_TEMPLATE.md:
--------------------------------------------------------------------------------
 1 | # Summary
 2 |
 3 | <!-- Facebook has a bounty program for the safe disclosure of security bugs. In
 4 | those cases, please go through the process outlined on that page and do not
 5 | file a public issue. -->
 6 |
 7 | # Platform
 8 |
 9 | <!-- if the question/problem is not platform-specific, please ignore this -->
10 |
11 | OS: <!-- e.g. macOS 10.13.3 -->
12 |
13 | Faiss version: <!-- git commit, e.g. 56383610bcb982d6591e2e2bea3516cb7723e04a -->
14 |
15 | Installed from: <!-- anaconda? compiled by yourself ? -->
16 |
17 | Faiss compilation options: <!-- e.g. using MKL with compile flags ... -->
18 |
19 | Running on:
20 | - [ ] CPU
21 | - [ ] GPU
22 |
23 | Interface:
24 | - [ ] C++
25 | - [ ] Python
26 |
27 | # Reproduction instructions
28 |
29 | <!-- Please provide specific and comprehensive instructions to reproduce the
30 | described behavior. -->
31 |
32 | <!-- Please *do not* post screenshots of logs. They are not searchable. Copy/paste
33 | the text or make a gist if the text is too bulky. -->
34 |


--------------------------------------------------------------------------------
/CHANGELOG.md:
--------------------------------------------------------------------------------
  1 | # Changelog
  2 | All notable changes to this project will be documented in this file.
  3 |
  4 | ## [Unreleased]
  5 |
  6 | ## [1.11.0] - 2025-04-24
  7 |
  8 |
  9 | Added
 10 | - RaBitQ implementation (#4235)
 11 | - Add RaBitQ to the swigfaiss so we can access its properties correctly in python (#4304)
 12 | - Add date and time to the codec file path so that the file doesn't get overridden with each run (#4303)
 13 | - Add missing header in faiss/CMakeLists.txt (#4285)
 14 | - Implement is_spherical and normalize_L2 booleans as part of the training APIs (#4279)
 15 | - Add normalize_l2 boolean to distributed training API
 16 | - re-land mmap diff (#4250)
 17 | - SearchParameters support for IndexBinaryFlat (#4055)
 18 | - Support non-partition col and map in the embedding reader (#4229)
 19 | - Support cosine distance for training vectors (#4227)
 20 | - Add missing #include in code_distance-sve.h (#4219)
 21 | - Add the support for IndexIDMap with Cagra index (#4188)
 22 | - Add bounds checking to hnsw nb_neighbors (#4185)
 23 | - Add sharding convenience function for IVF indexes (#4150)
 24 | - Added support for building for MinGW, in addition to MSVC (#4145)
 25 |
 26 | Changed
 27 | - Skip mmap test case in AIX. (#4275)
 28 | - Handle insufficient driver gracefully (#4271)
 29 | - relax input params for IndexIVFRaBitQ::get_InvertedListScanner() (#4270)
 30 | - Allow using custom index readers and writers (#4180)
 31 | - Upgrade to libcuvs=25.04 (#4164)
 32 | - ignore regex (#4264)
 33 | - Publish the C API to Conda (#4186)
 34 | - Pass row filters to Hive Reader to filter rows (#4256)
 35 | - Back out "test merge with internal repo" (#4244)
 36 | - test merge with internal repo (#4242)
 37 | - Revert D69972250: Memory-mapping and Zero-copy deserializers
 38 | - Revert D69984379: mem mapping and zero-copy python fixes
 39 | - mem mapping and zero-copy python fixes (#4212)
 40 | - Memory-mapping and Zero-copy deserializers (#4199)
 41 | - Use `nullptr` in faiss/gpu/StandardGpuResources.cpp (#4232)
 42 | - Make static method in header inline (#4214)
 43 | - Upgrade openblas to 0.3.29 for ARM architectures (#4203)
 44 | - Pass `store_dataset` argument along to cuVS CAGRA (#4173)
 45 | - Handle plain SearchParameters in HNSW searches (#4167)
 46 | - Update INSTALL.md to remove some raft references, add missing dependency (#4176)
 47 | - Update README.md (#4169)
 48 | - Update CAGRA docs (#4152)
 49 | - Expose IDSelectorBitmap in the C_API (#4158)
 50 |
 51 | Fixed
 52 | - fix: algorithm of spreading vectors over shards (#4299)
 53 | - Fix overflow of int32 in IndexNSG (#4297)
 54 | - Fix Type Error in Conditional Logic (#4294)
 55 | - faiss/gpu/GpuAutoTune.cpp: fix llvm-19-exposed -Wunused-but-set-variable warnings
 56 | - Fix nightly by pinning conda-build to prevent regression in 25.3.2 (#4287)
 57 | - Fix CQS signal. Id] 88153895 -- readability-redundant-string-init in fbcode/faiss (#4283)
 58 | - Fix a placeholder for 'unimplemented' in mapped_io.cpp (#4268)
 59 | - fix bug: IVFPQ of raft/cuvs does not require redundant check (#4241)
 60 | - fix a serialization problem in RaBitQ (#4261)
 61 | - Grammar fix in FlatIndexHNSW (#4253)
 62 | - Fix CUDA kernel index data type in faiss/gpu/impl/DistanceUtils.cuh +10 (#4246)
 63 | - fix `IVFPQFastScan::RangeSearch()` on the `ARM` architecture (#4247)
 64 | - fix integer overflow issue when calculating imbalance_factor (#4245)
 65 | - Fix bug with metric_arg in IndexHNSW (#4239)
 66 | - Address compile errors and warnings (#4238)
 67 | - faiss: fix non-templated hammings function (#4195)
 68 | - Fix LLVM-19 compilation issue in faiss/AutoTune.cpp (#4220)
 69 | - Fix cloning and reverse index factory for NSG indices (#4151)
 70 | - Remove python_abi to fix nightly (#4217)
 71 | - Fix IVF quantizer centroid sharding so IDs are generated (#4197)
 72 | - Pin lief to fix nightly (#4211)
 73 | - Fix Sapphire Rapids never loading in Python bindings (#4209)
 74 | - Attempt to nightly fix (#4204)
 75 | - Fix nightly by installing earlier version of lief (#4198)
 76 | - Check for not completed
 77 | - Fix install error when building avx512_spr variant (#4170)
 78 | - fix: gpu tests link failure with static lib (#4137)
 79 | - Fix the order of parameters in bench_scalar_quantizer_distance. (#4159)
 80 |
 81 | Deprecated
 82 | - Remove unused exception parameter from faiss/impl/ResultHandler.h (#4243)
 83 | - Remove unused variable (#4205)
 84 |
 85 |
 86 |
 87 | ## [1.10.0] - 2025-01-30
 88 |
 89 |
 90 | Added
 91 | - Add desc_name to dataset descriptor (#3935)
 92 | - implement ST_norm_from_LUT for the ResidualQuantizer (#3917)
 93 | - Add example of how to build, link, and test an external SWIG module (#3922)
 94 | - add copyright header (#3948)
 95 | - Add some SVE implementations (#3933)
 96 | - Enable linting: lint config changes plus arc lint command (#3966)
 97 | - Re-add example of how to build, link, and test an external SWIG module (#3981)
 98 | - demo: IndexPQ: separate codes from codebook (#3987)
 99 | - add all wrapped indexes to the index_read (#3988)
100 | - add validity check AlignedTableTightAlloc clear method (#3997)
101 | - Add index binary to telemetry (#4001)
102 | - Add VectorTransform read from filename to the C API (#3970)
103 | - Added IndexLSH to the demo (#4009)
104 | - write distributed_kmeans centroids and assignments to hive tables (#4017)
105 | - introduce data splits in dataset descriptor (#4012)
106 | - Faiss GPU: bfloat16 brute-force kNN support (#4018)
107 | - ROCm support for bfloat16 (#4039)
108 | - Unit tests for distances_simd.cpp (#4058)
109 | - add cuda-toolkit for GPU (#4057)
110 | - Add more unit testing for IndexHNSW [1/n] (#4054)
111 | - Add more unit testing for IndexHNSW [2/n] (#4056)
112 | - Add more unit testing for HNSW [3/n] (#4059)
113 | - Add more unit testing for HNSW [4/n] (#4061)
114 | - Add more unit tests for index_read and index_write (#4068)
115 | - Add testing for utils/hamming.cpp (#4079)
116 | - Test sa_decode methd on IndexIVFFlat (#4098)
117 | - Conditionally compile extras like benchmarks and demos (#4094)
118 | - Add a new architecture mode: 'avx512_spr'. (#4025)
119 | - Use _mm512_popcnt_epi64 to speedup hamming distance evaluation. (#4020)
120 | - PQ with pytorch (#4116)
121 | - add range_search() to IndexRefine (#4022)
122 | - Expose accumulate_to_mem from faiss interface (#4099)
123 | - Windows Arm64 support (#4087)
124 | - add test to cover GPU (#4130)
125 | - Added support for building without MKL (#4147)
126 |
127 | Changed
128 | - Move train, build and search to their respective operators (#3934)
129 | - PQFS into Index trainer (#3941)
130 | - Place a useful cmake function 'link_to_faiss_lib' into a separate file (#3939)
131 | - Cache device major version value to avoid multiple calls of getCudaDeviceProperties (#3950)
132 | - Consolidate set_target_properties() calls in faiss/CMakeLists.txt (#3973)
133 | - Removing Manual Hipify Build Step (#3962)
134 | - Allow to replace graph structure for NSG graphs (#3975)
135 | - Adjust nightly build (#3978)
136 | - Update RAFT CI with pytorch 2.4.1 (#3980)
137 | - Moved add_sa_codes, sa_code_size to Index, IndexBinary base classes (#3989)
138 | - Update autoclose.yml (#4000)
139 | - Migrate from RAFT to CUVS (#3549)
140 | - Pin to numpy<2 (#4033)
141 | - (1/n) - Preload datasets in manifold so that subsequent stages of training, indexing and search can use those instead of each trainer or indexer downloading data. (#4034)
142 | - Constrain conda version for Windows build (#4040)
143 | - Updates to faiss-gpu-cuvs nightly pkg (#4032)
144 | - pin the dependecies version for x86_64 (#4046)
145 | - pin arm64 dependency (#4060)
146 | - Pin conda build (#4062)
147 | - Improve naming due to codemod (#4063)
148 | - Improve naming due to codemod (#4064)
149 | - Improve naming due to codemod (#4065)
150 | - separare the github build into two conditions (#4066)
151 | - Improve naming due to codemod (#4070)
152 | - improve naming due to codemod (#4067)
153 | - improve naming due to codemod (#4071)
154 | - improve naming due to codemod (#4072)
155 | - fix nightily build (#4080)
156 | - Change github action workflows name (#4083)
157 | - Resolve Packaging Issues (#4044)
158 | - Update __init__.py (#4086)
159 | - Exhaustive IVF probing in scalar quantizer tests (#4075)
160 | - Pin Nightlies with testing on PR (#4088)
161 | - Update benchmarking library code to work for IdMap index as well (#4093)
162 | - Update action.yml (#4100)
163 | - Upgrade CUVS to 24.12 (#4021)
164 | - Link cuVS Docs (#4084)
165 | - Set KnnDescriptor.desc_name in the Benchmarking core framework in FAISS like other descriptors (#4109)
166 | - enable quiet mode for conda install (#4112)
167 | - Disable retry build (#4124)
168 | - Add ngpu default argument to knn_ground_truth (#4123)
169 | - Update code comment to reflect the range of IF from [1, k] (#4139)
170 | - Reenable auto retry workflow (#4140)
171 | - Migration off defaults to conda-forge channel (#4126)
172 | - Benchmarking Scripts for cuVS Index, more docs updates (#4117)
173 |
174 | Fixed
175 | - Fix total_rows (#3942)
176 | - Fix INSTALL.md due to failure of conflict resolving (#3915)
177 | - Back out "Add example of how to build, link, and test an external SWIG module" (#3954)
178 | - Fix shadowed variable in faiss/IndexPQ.cpp (#3959)
179 | - Fix shadowed variable in faiss/IndexIVFAdditiveQuantizer.cpp (#3958)
180 | - Fix shadowed variable in faiss/impl/HNSW.cpp (#3961)
181 | - Fix shadowed variable in faiss/impl/simd_result_handlers.h (#3960)
182 | - Fix shadowed variable in faiss/utils/NeuralNet.cpp (#3952)
183 | - Resolve "incorrect-portions-license" errors: add no license lint to top of GPU files with both licenses (#3965)
184 | - Resolve "duplicate-license-header": Find and replace duplicate license headers (#3967)
185 | - fix some more nvidia licenses that get erased (#3977)
186 | - fix merge_flat_ondisk stress run failures (#3999)
187 | - Fix reverse_index_factory formatting of ScalarQuantizers (#4003)
188 | - Fix shadowed variable in faiss/IndexAdditiveQuantizer.cpp (#4011)
189 | - facebook-unused-include-check in fbcode/faiss (#4029)
190 | - fix linter (#4035)
191 | - Some chore fixes (#4010)
192 | - Fix unused variable compilation error (#4041)
193 | - stop dealloc of coarse quantizer when it is deleted (#4045)
194 | - Fix SCD Table test flakiness (#4069)
195 | - Fix IndexIVFFastScan reconstruct_from_offset method (#4095)
196 | - more fast-scan reconstruction (#4128)
197 | - Fix nightly cuVS 11.8.0 failure (#4149)
198 | - Correct capitalization of FAISS to Faiss (#4155)
199 | - Fix cuVS 12.4.0 nightly failure (#4153)
200 |
201 | Deprecated
202 | - Remove unused-variable in dumbo/backup/dumbo/service/tests/ChainReplicatorTests.cpp (#4024)
203 | - remove inconsistent oom exception test (#4052)
204 | - Remove unused(and wrong) io macro (#4122)
205 |
206 |
207 | ## [1.9.0] - 2024-10-04
208 | ### Added
209 | - Add AVX-512 implementation for the distance and scalar quantizer functions. (#3853)
210 | - Allow k and M suffixes in IVF indexes (#3812)
211 | - add reconstruct support to additive quantizers (#3752)
212 | - introduce options for reducing the overhead for a clustering procedure (#3731)
213 | - Add hnsw search params for bounded queue option (#3748)
214 | - ROCm support (#3462)
215 | - Add sve targets (#2886)
216 | - add get_version() for c_api (#3688)
217 | - QINCo implementation in CPU Faiss (#3608)
218 | - Add search functionality to FlatCodes (#3611)
219 | - add dispatcher for VectorDistance and ResultHandlers (#3627)
220 | - Add SQ8bit signed quantization (#3501)
221 | - Add ABS_INNER_PRODUCT metric (#3524)
222 | - Interop between CAGRA and HNSW (#3252)
223 | - add skip_storage flag to HNSW (#3487)
224 | - QT_bf16 for scalar quantizer for bfloat16 (#3444)
225 | - Implement METRIC.NaNEuclidean (#3414)
226 | - TimeoutCallback C++ and Python (#3417)
227 | - support big-endian machines (#3361)
228 | - Support for Remove ids from IVFPQFastScan index (#3354)
229 | - Implement reconstruct_n for GPU IVFFlat indexes (#3338)
230 | - Support of skip_ids in merge_from_multiple function of OnDiskInvertedLists (#3327)
231 | - Add the ability to clone and read binary indexes to the C API. (#3318)
232 | - AVX512 for PQFastScan (#3276)
233 |
234 | ### Changed
235 | - faster hnsw CPU index training (#3822)
236 | - Some small improvements. (#3692)
237 | - First attempt at LSH matching with nbits (#3679)
238 | - Set verbosoe before train (#3619)
239 | - Remove duplicate NegativeDistanceComputer instances (#3450)
240 | - interrupt for NNDescent (#3432)
241 | - Get rid of redundant instructions in ScalarQuantizer (#3430)
242 | - PowerPC, improve code generation for function fvec_L2sqr (#3416)
243 | - Unroll loop in lookup_2_lanes (#3364)
244 | - Improve filtering & search parameters propagation (#3304)
245 | - Change index_cpu_to_gpu to throw for indices not implemented on GPU (#3336)
246 | - Throw when attempting to move IndexPQ to GPU (#3328)
247 | - Skip HNSWPQ sdc init with new io flag (#3250)
248 |
249 | ### Fixed
250 | - FIx a bug for a non-simdlib code of ResidualQuantizer (#3868)
251 | - assign_index should default to null (#3855)
252 | - Fix an incorrectly counted the number of computed distances for HNSW (#3840)
253 | - Add error for overflowing nbits during PQ construction (#3833)
254 | - Fix radius search with HSNW and IP (#3698)
255 | - fix algorithm of spreading vectors over shards (#3374)
256 | - Fix IndexBinary.assign Python method (#3384)
257 | - Few fixes in bench_fw to enable IndexFromCodec (#3383)
258 | - Fix the endianness issue in AIX while running the benchmark. (#3345)
259 | - Fix faiss swig build with version > 4.2.x (#3315)
260 | - Fix problems when using 64-bit integers. (#3322)
261 | - Fix IVFPQFastScan decode function (#3312)
262 | - Handling FaissException in few destructors of ResultHandler.h (#3311)
263 | - Fix HNSW stats (#3309)
264 | - AIX compilation fix for io classes (#3275)
265 |
266 |
267 | ## [1.8.0] - 2024-02-27
268 | ### Added
269 | - Added a new conda package faiss-gpu-raft alongside faiss-cpu and faiss-gpu
270 | - Integrated IVF-Flat and IVF-PQ implementations in faiss-gpu-raft from RAFT by Nvidia [thanks Corey Nolet and Tarang Jain]
271 | - Added a context parameter to InvertedLists and InvertedListsIterator
272 | - Added Faiss on Rocksdb demo to showing how inverted lists can be persisted in a key-value store
273 | - Introduced Offline IVF framework powered by Faiss big batch search
274 | - Added SIMD NEON Optimization for QT_FP16 in Scalar Quantizer. [thanks Naveen Tatikonda]
275 | - Generalized ResultHandler and supported range search for HNSW and FastScan
276 | - Introduced avx512 optimization mode and FAISS_OPT_LEVEL env variable [thanks Alexandr Ghuzva]
277 | - Added search parameters for IndexRefine::search() and IndexRefineFlat::search()
278 | - Supported large two-level clustering
279 | - Added support for Python 3.11 and 3.12
280 | - Added support for CUDA 12
281 |
282 | ### Changed
283 | - Used the benchmark to find Pareto optimal indices. Intentionally limited to IVF(Flat|HNSW),PQ|SQ indices
284 | - Splitted off RQ encoding steps to another file
285 | - Supported better NaN handling
286 | - HNSW speedup + Distance 4 points [thanks Alexandr Ghuzva]
287 |
288 | ### Fixed
289 | - Fixed DeviceVector reallocations in Faiss GPU
290 | - Used efSearch from params if provided in HNSW search
291 | - Fixed warp synchronous behavior in Faiss GPU CUDA 12
292 |
293 |
294 | ## [1.7.4] - 2023-04-12
295 | ### Added
296 | - Added big batch IVF search for conducting efficient search with big batches of queries
297 | - Checkpointing in big batch search support
298 | - Precomputed centroids support
299 | - Support for iterable inverted lists for eg. key value stores
300 | - 64-bit indexing arithmetic support in FAISS GPU
301 | - IndexIVFShards now handle IVF indexes with a common quantizer
302 | - Jaccard distance support
303 | - CodePacker for non-contiguous code layouts
304 | - Approximate evaluation of top-k distances for ResidualQuantizer and IndexBinaryFlat
305 | - Added support for 12-bit PQ / IVFPQ fine quantizer decoders for standalone vector codecs (faiss/cppcontrib)
306 | - Conda packages for osx-arm64 (Apple M1) and linux-aarch64 (ARM64) architectures
307 | - Support for Python 3.10
308 |
309 | ### Removed
310 | - CUDA 10 is no longer supported in precompiled packages
311 | - Removed Python 3.7 support for precompiled packages
312 | - Removed constraint for using fine quantizer with no greater than 8 bits for IVFPQ, for example, now it is possible to use IVF256,PQ10x12 for a CPU index
313 |
314 | ### Changed
315 | - Various performance optimizations for PQ / IVFPQ for AVX2 and ARM for training (fused distance+nearest kernel), search (faster kernels for distance_to_code() and scan_list_*()) and vector encoding
316 | - A magnitude faster CPU code for LSQ/PLSQ training and vector encoding (reworked code)
317 | - Performance improvements for Hamming Code computations for AVX2 and ARM (reworked code)
318 | - Improved auto-vectorization support for IP and L2 distance computations (better handling of pragmas)
319 | - Improved ResidualQuantizer vector encoding (pooling memory allocations, avoid r/w to a temporary buffer)
320 |
321 | ### Fixed
322 | - HSNW bug fixed which improves the recall rate! Special thanks to zh Wang @hhy3 for this.
323 | - Faiss GPU IVF large query batch fix
324 | - Faiss + Torch fixes, re-enable k = 2048
325 | - Fix the number of distance computations to match max_codes parameter
326 | - Fix decoding of large fast_scan blocks
327 |
328 |
329 | ## [1.7.3] - 2022-11-3
330 | ### Added
331 | - Added sparse k-means routines and moved the generic kmeans to contrib
332 | - Added FlatDistanceComputer for all FlatCodes indexes
333 | - Support for fast accumulation of 4-bit LSQ and RQ
334 | - Added product additive quantization
335 | - Support per-query search parameters for many indexes + filtering by ids
336 | - write_VectorTransform and read_vectorTransform were added to the public API (by @AbdelrahmanElmeniawy)
337 | - Support for IDMap2 in index_factory by adding "IDMap2" to prefix or suffix of the input String (by @AbdelrahmanElmeniawy)
338 | - Support for merging all IndexFlatCodes descendants (by @AbdelrahmanElmeniawy)
339 | - Remove and merge features for IndexFastScan (by @AbdelrahmanElmeniawy)
340 | - Performance improvements: 1) specialized the AVX2 pieces of code speeding up certain hotspots, 2) specialized kernels for vector codecs (this can be found in faiss/cppcontrib)
341 |
342 |
343 | ### Fixed
344 | - Fixed memory leak in OnDiskInvertedLists::do_mmap when the file is not closed (by @AbdelrahmanElmeniawy)
345 | - LSH correctly throws error for metric types other than METRIC_L2 (by @AbdelrahmanElmeniawy)
346 |
347 | ## [1.7.2] - 2021-12-15
348 | ### Added
349 | - Support LSQ on GPU (by @KinglittleQ)
350 | - Support for exact 1D kmeans (by @KinglittleQ)
351 |
352 | ## [1.7.1] - 2021-05-27
353 | ### Added
354 | - Support for building C bindings through the `FAISS_ENABLE_C_API` CMake option.
355 | - Serializing the indexes with the python pickle module
356 | - Support for the NNDescent k-NN graph building method (by @KinglittleQ)
357 | - Support for the NSG graph indexing method (by @KinglittleQ)
358 | - Residual quantizers: support as codec and unoptimized search
359 | - Support for 4-bit PQ implementation for ARM (by @vorj, @n-miyamoto-fixstars, @LWisteria, and @matsui528)
360 | - Implementation of Local Search Quantization (by @KinglittleQ)
361 |
362 | ### Changed
363 | - The order of xb an xq was different between `faiss.knn` and `faiss.knn_gpu`.
364 | Also the metric argument was called distance_type.
365 | - The typed vectors (LongVector, LongLongVector, etc.) of the SWIG interface have
366 | been deprecated. They have been replaced with Int32Vector, Int64Vector, etc. (by h-vetinari)
367 |
368 | ### Fixed
369 | - Fixed a bug causing kNN search functions for IndexBinaryHash and
370 | IndexBinaryMultiHash to return results in a random order.
371 | - Copy constructor of AlignedTable had a bug leading to crashes when cloning
372 | IVFPQ indices.
373 |
374 | ## [1.7.0] - 2021-01-27
375 |
376 | ## [1.6.5] - 2020-11-22
377 |
378 | ## [1.6.4] - 2020-10-12
379 | ### Added
380 | - Arbitrary dimensions per sub-quantizer now allowed for `GpuIndexIVFPQ`.
381 | - Brute-force kNN on GPU (`bfKnn`) now accepts `int32` indices.
382 | - Nightly conda builds now available (for CPU).
383 | - Faiss is now supported on Windows.
384 |
385 | ## [1.6.3] - 2020-03-24
386 | ### Added
387 | - Support alternative distances on GPU for GpuIndexFlat, including L1, Linf and
388 | Lp metrics.
389 | - Support METRIC_INNER_PRODUCT for GpuIndexIVFPQ.
390 | - Support float16 coarse quantizer for GpuIndexIVFFlat and GpuIndexIVFPQ. GPU
391 | Tensor Core operations (mixed-precision arithmetic) are enabled on supported
392 | hardware when operating with float16 data.
393 | - Support k-means clustering with encoded vectors. This makes it possible to
394 | train on larger datasets without decompressing them in RAM, and is especially
395 | useful for binary datasets (see https://github.com/facebookresearch/faiss/blob/main/tests/test_build_blocks.py#L92).
396 | - Support weighted k-means. Weights can be associated to each training point
397 | (see https://github.com/facebookresearch/faiss/blob/main/tests/test_build_blocks.py).
398 | - Serialize callback in python, to write to pipes or sockets (see
399 | https://github.com/facebookresearch/faiss/wiki/Index-IO,-cloning-and-hyper-parameter-tuning).
400 | - Reconstruct arbitrary ids from IndexIVF + efficient remove of a small number
401 | of ids. This avoids 2 inefficiencies: O(ntotal) removal of vectors and
402 | IndexIDMap2 on top of indexIVF. Documentation here:
403 | https://github.com/facebookresearch/faiss/wiki/Special-operations-on-indexes.
404 | - Support inner product as a metric in IndexHNSW (see
405 | https://github.com/facebookresearch/faiss/blob/main/tests/test_index.py#L490).
406 | - Support PQ of sizes other than 8 bit in IndexIVFPQ.
407 | - Demo on how to perform searches sequentially on an IVF index. This is useful
408 | for an OnDisk index with a very large batch of queries. In that case, it is
409 | worthwhile to scan the index sequentially (see
410 | https://github.com/facebookresearch/faiss/blob/main/tests/test_ivflib.py#L62).
411 | - Range search support for most binary indexes.
412 | - Support for hashing-based binary indexes (see
413 | https://github.com/facebookresearch/faiss/wiki/Binary-indexes).
414 |
415 | ### Changed
416 | - Replaced obj table in Clustering object: now it is a ClusteringIterationStats
417 | structure that contains additional statistics.
418 |
419 | ### Removed
420 | - Removed support for useFloat16Accumulator for accumulators on GPU (all
421 | accumulations are now done in float32, regardless of whether float16 or float32
422 | input data is used).
423 |
424 | ### Fixed
425 | - Some python3 fixes in benchmarks.
426 | - Fixed GpuCloner (some fields were not copied, default to no precomputed tables
427 | with IndexIVFPQ).
428 | - Fixed support for new pytorch versions.
429 | - Serialization bug with alternative distances.
430 | - Removed test on multiple-of-4 dimensions when switching between blas and AVX
431 | implementations.
432 |
433 | ## [1.6.2] - 2020-03-10
434 |
435 | ## [1.6.1] - 2019-12-04
436 |
437 | ## [1.6.0] - 2019-09-24
438 | ### Added
439 | - Faiss as a codec: We introduce a new API within Faiss to encode fixed-size
440 | vectors into fixed-size codes. The encoding is lossy and the tradeoff between
441 | compression and reconstruction accuracy can be adjusted.
442 | - ScalarQuantizer support for GPU, see gpu/GpuIndexIVFScalarQuantizer.h. This is
443 | particularly useful as GPU memory is often less abundant than CPU.
444 | - Added easy-to-use serialization functions for indexes to byte arrays in Python
445 | (faiss.serialize_index, faiss.deserialize_index).
446 | - The Python KMeans object can be used to use the GPU directly, just add
447 | gpu=True to the constuctor see gpu/test/test_gpu_index.py test TestGPUKmeans.
448 |
449 | ### Changed
450 | - Change in the code layout: many C++ sources are now in subdirectories impl/
451 | and utils/.
452 |
453 | ## [1.5.3] - 2019-06-24
454 | ### Added
455 | - Basic support for 6 new metrics in CPU IndexFlat and IndexHNSW (https://github.com/facebookresearch/faiss/issues/848).
456 | - Support for IndexIDMap/IndexIDMap2 with binary indexes (https://github.com/facebookresearch/faiss/issues/780).
457 |
458 | ### Changed
459 | - Throw python exception for OOM (https://github.com/facebookresearch/faiss/issues/758).
460 | - Make DistanceComputer available for all random access indexes.
461 | - Gradually moving from long to uint64_t for portability.
462 |
463 | ### Fixed
464 | - Slow scanning of inverted lists (https://github.com/facebookresearch/faiss/issues/836).
465 |
466 | ## [1.5.2] - 2019-05-28
467 | ### Added
468 | - Support for searching several inverted lists in parallel (parallel_mode != 0).
469 | - Better support for PQ codes where nbit != 8 or 16.
470 | - IVFSpectralHash implementation: spectral hash codes inside an IVF.
471 | - 6-bit per component scalar quantizer (4 and 8 bit were already supported).
472 | - Combinations of inverted lists: HStackInvertedLists and VStackInvertedLists.
473 | - Configurable number of threads for OnDiskInvertedLists prefetching (including
474 | 0=no prefetch).
475 | - More test and demo code compatible with Python 3 (print with parentheses).
476 |
477 | ### Changed
478 | - License was changed from BSD+Patents to MIT.
479 | - Exceptions raised in sub-indexes of IndexShards and IndexReplicas are now
480 | propagated.
481 | - Refactored benchmark code: data loading is now in a single file.
482 |
483 | ## [1.5.1] - 2019-04-05
484 | ### Added
485 | - MatrixStats object, which reports useful statistics about a dataset.
486 | - Option to round coordinates during k-means optimization.
487 | - An alternative option for search in HNSW.
488 | - Support for range search in IVFScalarQuantizer.
489 | - Support for direct uint_8 codec in ScalarQuantizer.
490 | - Better support for PQ code assignment with external index.
491 | - Support for IMI2x16 (4B virtual centroids).
492 | - Support for k = 2048 search on GPU (instead of 1024).
493 | - Support for renaming an ondisk invertedlists.
494 | - Support for nterrupting computations with interrupt signal (ctrl-C) in python.
495 | - Simplified build system (with --with-cuda/--with-cuda-arch options).
496 |
497 | ### Changed
498 | - Moved stats() and imbalance_factor() from IndexIVF to InvertedLists object.
499 | - Renamed IndexProxy to IndexReplicas.
500 | - Most CUDA mem alloc failures now throw exceptions instead of terminating on an
501 | assertion.
502 | - Updated example Dockerfile.
503 | - Conda packages now depend on the cudatoolkit packages, which fixes some
504 | interferences with pytorch. Consequentially, faiss-gpu should now be installed
505 | by conda install -c pytorch faiss-gpu cudatoolkit=10.0.
506 |
507 | ## [1.5.0] - 2018-12-19
508 | ### Added
509 | - New GpuIndexBinaryFlat index.
510 | - New IndexBinaryHNSW index.
511 |
512 | ## [1.4.0] - 2018-08-30
513 | ### Added
514 | - Automatic tracking of C++ references in Python.
515 | - Support for non-intel platforms, some functions optimized for ARM.
516 | - Support for overriding nprobe for concurrent searches.
517 | - Support for floating-point quantizers in binary indices.
518 |
519 | ### Fixed
520 | - No more segfaults due to Python's GC.
521 | - GpuIndexIVFFlat issues for float32 with 64 / 128 dims.
522 | - Sharding of flat indexes on GPU with index_cpu_to_gpu_multiple.
523 |
524 | ## [1.3.0] - 2018-07-10
525 | ### Added
526 | - Support for binary indexes (IndexBinaryFlat, IndexBinaryIVF).
527 | - Support fp16 encoding in scalar quantizer.
528 | - Support for deduplication in IndexIVFFlat.
529 | - Support for index serialization.
530 |
531 | ### Fixed
532 | - MMAP bug for normal indices.
533 | - Propagation of io_flags in read func.
534 | - k-selection for CUDA 9.
535 | - Race condition in OnDiskInvertedLists.
536 |
537 | ## [1.2.1] - 2018-02-28
538 | ### Added
539 | - Support for on-disk storage of IndexIVF data.
540 | - C bindings.
541 | - Extended tutorial to GPU indices.
542 |
543 | [Unreleased]: https://github.com/facebookresearch/faiss/compare/v1.11.0...HEAD
544 | [1.11.0]: https://github.com/facebookresearch/faiss/compare/v1.10.0...v1.11.0
545 | [1.10.0]: https://github.com/facebookresearch/faiss/compare/v1.9.0...v1.10.0
546 | [1.9.0]: https://github.com/facebookresearch/faiss/compare/v1.8.0...v1.9.0
547 | [1.8.0]: https://github.com/facebookresearch/faiss/compare/v1.7.4...v1.8.0
548 | [1.7.4]: https://github.com/facebookresearch/faiss/compare/v1.7.3...v1.7.4
549 | [1.7.3]: https://github.com/facebookresearch/faiss/compare/v1.7.2...v1.7.3
550 | [1.7.2]: https://github.com/facebookresearch/faiss/compare/v1.7.1...v1.7.2
551 | [1.7.1]: https://github.com/facebookresearch/faiss/compare/v1.7.0...v1.7.1
552 | [1.7.0]: https://github.com/facebookresearch/faiss/compare/v1.6.5...v1.7.0
553 | [1.6.5]: https://github.com/facebookresearch/faiss/compare/v1.6.4...v1.6.5
554 | [1.6.4]: https://github.com/facebookresearch/faiss/compare/v1.6.3...v1.6.4
555 | [1.6.3]: https://github.com/facebookresearch/faiss/compare/v1.6.2...v1.6.3
556 | [1.6.2]: https://github.com/facebookresearch/faiss/compare/v1.6.1...v1.6.2
557 | [1.6.1]: https://github.com/facebookresearch/faiss/compare/v1.6.0...v1.6.1
558 | [1.6.0]: https://github.com/facebookresearch/faiss/compare/v1.5.3...v1.6.0
559 | [1.5.3]: https://github.com/facebookresearch/faiss/compare/v1.5.2...v1.5.3
560 | [1.5.2]: https://github.com/facebookresearch/faiss/compare/v1.5.1...v1.5.2
561 | [1.5.1]: https://github.com/facebookresearch/faiss/compare/v1.5.0...v1.5.1
562 | [1.5.0]: https://github.com/facebookresearch/faiss/compare/v1.4.0...v1.5.0
563 | [1.4.0]: https://github.com/facebookresearch/faiss/compare/v1.3.0...v1.4.0
564 | [1.3.0]: https://github.com/facebookresearch/faiss/compare/v1.2.1...v1.3.0
565 | [1.2.1]: https://github.com/facebookresearch/faiss/releases/tag/v1.2.1
566 |


--------------------------------------------------------------------------------
/CODE_OF_CONDUCT.md:
--------------------------------------------------------------------------------
1 | # Code of Conduct
2 | Facebook has adopted a Code of Conduct that we expect project participants to adhere to. Please [read the full text](https://code.fb.com/codeofconduct) so that you can understand what actions will and will not be tolerated.


--------------------------------------------------------------------------------
/CONTRIBUTING.md:
--------------------------------------------------------------------------------
 1 | # Contributing to Faiss
 2 |
 3 | We want to make contributing to this project as easy and transparent as
 4 | possible.
 5 |
 6 | ## Our Development Process
 7 |
 8 | We mainly develop Faiss within Facebook. Sometimes, we will sync the
 9 | github version of Faiss with the internal state.
10 |
11 | ## Pull Requests
12 |
13 | We welcome pull requests that add significant value to Faiss. If you plan to do
14 | a major development and contribute it back to Faiss, please contact us first before
15 | putting too much effort into it.
16 |
17 | 1. Fork the repo and create your branch from `main`.
18 | 2. If you've added code that should be tested, add tests.
19 | 3. If you've changed APIs, update the documentation.
20 | 4. Ensure the test suite passes.
21 | 5. Make sure your code lints.
22 | 6. If you haven't already, complete the Contributor License Agreement ("CLA").
23 |
24 | There is a Facebook internal test suite for Faiss, and we need to run
25 | all changes to Faiss through it.
26 |
27 | ## Contributor License Agreement ("CLA")
28 |
29 | In order to accept your pull request, we need you to submit a CLA. You only need
30 | to do this once to work on any of Facebook's open source projects.
31 |
32 | Complete your CLA here: <https://code.facebook.com/cla>
33 |
34 | ## Issues
35 |
36 | We use GitHub issues to track public bugs. Please ensure your description is
37 | clear and has sufficient instructions to be able to reproduce the issue.
38 |
39 | Facebook has a [bounty program](https://www.facebook.com/whitehat/) for the safe
40 | disclosure of security bugs. In those cases, please go through the process
41 | outlined on that page and do not file a public issue.
42 |
43 | ## Coding Style
44 |
45 | * 4 spaces for indentation in C++ (no tabs)
46 | * 80 character line length (both for C++ and Python)
47 | * C++ language level: C++17
48 |
49 | ## License
50 |
51 | By contributing to Faiss, you agree that your contributions will be licensed
52 | under the LICENSE file in the root directory of this source tree.
53 |


--------------------------------------------------------------------------------
/INSTALL.md:
--------------------------------------------------------------------------------
  1 | # Installing Faiss via conda
  2 |
  3 | The supported way to install Faiss is through [conda](https://docs.conda.io).
  4 | Stable releases are pushed regularly to the pytorch conda channel, as well as
  5 | pre-release nightly builds.
  6 |
  7 | - The CPU-only faiss-cpu conda package is currently available on Linux (x86-64 and aarch64), OSX (arm64 only), and Windows (x86-64)
  8 | - faiss-gpu, containing both CPU and GPU indices, is available on Linux (x86-64 only) for CUDA 11.4 and 12.1
  9 | - faiss-gpu-cuvs package containing GPU indices provided by [NVIDIA cuVS](https://github.com/rapidsai/cuvs/) version 24.12, is available on Linux (x86-64 only) for CUDA 11.8 and 12.4.
 10 |
 11 | To install the latest stable release:
 12 |
 13 | ``` shell
 14 | # CPU-only version
 15 | $ conda install -c pytorch faiss-cpu=1.11.0
 16 |
 17 | # GPU(+CPU) version
 18 | $ conda install -c pytorch -c nvidia faiss-gpu=1.11.0
 19 |
 20 | # GPU(+CPU) version with NVIDIA cuVS
 21 | $ conda install -c pytorch -c nvidia -c rapidsai -c conda-forge libnvjitlink faiss-gpu-cuvs=1.11.0
 22 |
 23 | # GPU(+CPU) version using AMD ROCm not yet available
 24 | ```
 25 |
 26 | For faiss-gpu, the nvidia channel is required for CUDA, which is not published in the main anaconda channel.
 27 |
 28 | For faiss-gpu-cuvs, the rapidsai, conda-forge and nvidia channels are required.
 29 |
 30 | Nightly pre-release packages can be installed as follows:
 31 |
 32 | ``` shell
 33 | # CPU-only version
 34 | $ conda install -c pytorch/label/nightly faiss-cpu
 35 |
 36 | # GPU(+CPU) version
 37 | $ conda install -c pytorch/label/nightly -c nvidia faiss-gpu=1.11.0
 38 |
 39 | # GPU(+CPU) version with NVIDIA cuVS (package built with CUDA 12.4)
 40 | conda install -c pytorch -c rapidsai -c rapidsai-nightly -c conda-forge -c nvidia pytorch/label/nightly::faiss-gpu-cuvs 'cuda-version>=12.0,<=12.5'
 41 |
 42 | # GPU(+CPU) version with NVIDIA cuVS (package built with CUDA 11.8)
 43 | conda install -c pytorch -c rapidsai -c rapidsai-nightly -c conda-forge -c nvidia pytorch/label/nightly::faiss-gpu-cuvs 'cuda-version>=11.4,<=11.8'
 44 |
 45 | # GPU(+CPU) version using AMD ROCm not yet available
 46 | ```
 47 | In the above commands, pytorch-cuda=11 or pytorch-cuda=12 would select a specific CUDA version, if it’s required.
 48 |
 49 | A combination of versions that installs GPU Faiss with CUDA and Pytorch (as of 2024-05-15):
 50 | ```
 51 | conda create --name faiss_1.8.0
 52 | conda activate faiss_1.8.0
 53 | conda install -c pytorch -c nvidia faiss-gpu=1.8.0 pytorch=*=*cuda* pytorch-cuda=11 numpy
 54 | ```
 55 |
 56 | ## Installing from conda-forge
 57 |
 58 | Faiss is also being packaged by [conda-forge](https://conda-forge.org/), the
 59 | community-driven packaging ecosystem for conda. The packaging effort is
 60 | collaborating with the Faiss team to ensure high-quality package builds.
 61 |
 62 | Due to the comprehensive infrastructure of conda-forge, it may even happen that
 63 | certain build combinations are supported in conda-forge that are not available
 64 | through the pytorch channel. To install, use
 65 |
 66 | ``` shell
 67 | # CPU version
 68 | $ conda install -c conda-forge faiss-cpu
 69 |
 70 | # GPU version
 71 | $ conda install -c conda-forge faiss-gpu
 72 |
 73 | # NVIDIA cuVS and AMD ROCm version not yet available
 74 | ```
 75 |
 76 | You can tell which channel your conda packages come from by using `conda list`.
 77 | If you are having problems using a package built by conda-forge, please raise
 78 | an [issue](https://github.com/conda-forge/faiss-split-feedstock/issues) on the
 79 | conda-forge package "feedstock".
 80 |
 81 | # Building from source
 82 |
 83 | Faiss can be built from source using CMake.
 84 |
 85 | Faiss is supported on x86-64 machines on Linux, OSX, and Windows. It has been
 86 | found to run on other platforms as well, see
 87 | [other platforms](https://github.com/facebookresearch/faiss/wiki/Related-projects#bindings-to-other-languages-and-porting-to-other-platforms).
 88 |
 89 | The basic requirements are:
 90 | - a C++17 compiler (with support for OpenMP support version 2 or higher),
 91 | - a BLAS implementation (on Intel machines we strongly recommend using Intel MKL for best
 92 | performance).
 93 |
 94 | The optional requirements are:
 95 | - for GPU indices:
 96 |   - nvcc,
 97 |   - the CUDA toolkit,
 98 | - for AMD GPUs:
 99 |   - AMD ROCm,
100 | - for using NVIDIA cuVS implementations:
101 |   - libcuvs=24.12
102 | - for the python bindings:
103 |   - python 3,
104 |   - numpy,
105 |   - and swig.
106 |
107 | Indications for specific configurations are available in the [troubleshooting
108 | section of the wiki](https://github.com/facebookresearch/faiss/wiki/Troubleshooting).
109 |
110 | ### Building with NVIDIA cuVS
111 |
112 | [cuVS](https://docs.rapids.ai/api/cuvs/nightly/) contains state-of-the-art implementations of several algorithms for running approximate nearest neighbors and clustering on the GPU. It is built on top of the [RAPIDS RAFT](https://github.com/rapidsai/raft) library of high performance machine learning primitives. Building Faiss with cuVS enabled allows a user to choose between regular GPU implementations in Faiss and cuVS implementations for specific algorithms.
113 |
114 | The libcuvs dependency should be installed via conda:
115 | 1. With CUDA 12.0 - 12.5:
116 | ```
117 | conda install -c rapidsai -c conda-forge -c nvidia libcuvs=24.12 'cuda-version>=12.0,<=12.5'
118 | ```
119 | 2. With CUDA 11.4 - 11.8
120 | ```
121 | conda install -c rapidsai -c conda-forge -c nvidia libcuvs=24.12 'cuda-version>=11.4,<=11.8'
122 | ```
123 | For more ways to install cuVS 24.12, refer to the [RAPIDS Installation Guide](https://docs.rapids.ai/install).
124 |
125 | ## Step 1: invoking CMake
126 |
127 | ``` shell
128 | $ cmake -B build .
129 | ```
130 |
131 | This generates the system-dependent configuration/build files in the `build/`
132 | subdirectory.
133 |
134 | Several options can be passed to CMake, among which:
135 | - general options:
136 |   - `-DFAISS_ENABLE_GPU=OFF` in order to disable building GPU indices (possible
137 |   values are `ON` and `OFF`),
138 |   - `-DFAISS_ENABLE_PYTHON=OFF` in order to disable building python bindings
139 |   (possible values are `ON` and `OFF`),
140 |   - `-DFAISS_ENABLE_CUVS=ON` in order to use the NVIDIA cuVS implementations
141 |     of the IVF-Flat, IVF-PQ and [CAGRA](https://arxiv.org/pdf/2308.15136) GPU-accelerated indices (default is `OFF`, possible, values are `ON` and `OFF`).
142 |     Note: `-DFAISS_ENABLE_GPU` must be set to `ON` when enabling this option.
143 |   - `-DBUILD_TESTING=OFF` in order to disable building C++ tests,
144 |   - `-DBUILD_SHARED_LIBS=ON` in order to build a shared library (possible values
145 |   are `ON` and `OFF`),
146 |   - `-DFAISS_ENABLE_C_API=ON` in order to enable building [C API](c_api/INSTALL.md) (possible values
147 |     are `ON` and `OFF`),
148 | - optimization-related options:
149 |   - `-DCMAKE_BUILD_TYPE=Release` in order to enable generic compiler
150 |   optimization options (enables `-O3` on gcc for instance),
151 |   - `-DFAISS_OPT_LEVEL=avx2` in order to enable the required compiler flags to
152 |   generate code using optimized SIMD/Vector instructions. Possible values are below:
153 |     - On x86-64, `generic`, `avx2`, 'avx512', and `avx512_spr` (for avx512 features available since Intel(R) Sapphire Rapids), by increasing order of optimization,
154 |     - On aarch64, `generic` and `sve`, by increasing order of optimization,
155 |   - `-DFAISS_USE_LTO=ON` in order to enable [Link-Time Optimization](https://en.wikipedia.org/wiki/Link-time_optimization) (default is `OFF`, possible values are `ON` and `OFF`).
156 | - BLAS-related options:
157 |   - `-DBLA_VENDOR=Intel10_64_dyn -DMKL_LIBRARIES=/path/to/mkl/libs` to use the
158 |   Intel MKL BLAS implementation, which is significantly faster than OpenBLAS
159 |   (more information about the values for the `BLA_VENDOR` option can be found in
160 |   the [CMake docs](https://cmake.org/cmake/help/latest/module/FindBLAS.html)),
161 | - GPU-related options:
162 |   - `-DCUDAToolkit_ROOT=/path/to/cuda-10.1` in order to hint to the path of
163 |   the CUDA toolkit (for more information, see
164 |   [CMake docs](https://cmake.org/cmake/help/latest/module/FindCUDAToolkit.html)),
165 |   - `-DCMAKE_CUDA_ARCHITECTURES="75;72"` for specifying which GPU architectures
166 |   to build against (see [CUDA docs](https://developer.nvidia.com/cuda-gpus) to
167 |   determine which architecture(s) you should pick),
168 |   - `-DFAISS_ENABLE_ROCM=ON` in order to enable building GPU indices for AMD GPUs.
169 |  `-DFAISS_ENABLE_GPU` must be `ON` when using this option. (possible values are `ON` and `OFF`),
170 | - python-related options:
171 |   - `-DPython_EXECUTABLE=/path/to/python3.7` in order to build a python
172 |   interface for a different python than the default one (see
173 |   [CMake docs](https://cmake.org/cmake/help/latest/module/FindPython.html)).
174 |
175 | ## Step 2: Invoking Make
176 |
177 | ``` shell
178 | $ make -C build -j faiss
179 | ```
180 |
181 | This builds the C++ library (`libfaiss.a` by default, and `libfaiss.so` if
182 | `-DBUILD_SHARED_LIBS=ON` was passed to CMake).
183 |
184 | The `-j` option enables parallel compilation of multiple units, leading to a
185 | faster build, but increasing the chances of running out of memory, in which case
186 | it is recommended to set the `-j` option to a fixed value (such as `-j4`).
187 |
188 | If making use of optimization options, build the correct target before swigfaiss.
189 |
190 | For AVX2:
191 |
192 | ``` shell
193 | $ make -C build -j faiss_avx2
194 | ```
195 |
196 | For AVX512:
197 |
198 | ``` shell
199 | $ make -C build -j faiss_avx512
200 | ```
201 |
202 | For AVX512 features available since Intel(R) Sapphire Rapids.
203 |
204 | ``` shell
205 | $ make -C build -j faiss_avx512_spr
206 | ```
207 |
208 | This will ensure the creation of neccesary files when building and installing the python package.
209 |
210 | ## Step 3: Building the python bindings (optional)
211 |
212 | ``` shell
213 | $ make -C build -j swigfaiss
214 | $ (cd build/faiss/python && python setup.py install)
215 | ```
216 |
217 | The first command builds the python bindings for Faiss, while the second one
218 | generates and installs the python package.
219 |
220 |
221 | ## Step 4: Installing the C++ library and headers (optional)
222 |
223 | ``` shell
224 | $ make -C build install
225 | ```
226 |
227 | This will make the compiled library (either `libfaiss.a` or `libfaiss.so` on
228 | Linux) available system-wide, as well as the C++ headers. This step is not
229 | needed to install the python package only.
230 |
231 |
232 | ## Step 5: Testing (optional)
233 |
234 | ### Running the C++ test suite
235 |
236 | To run the whole test suite, make sure that `cmake` was invoked with
237 | `-DBUILD_TESTING=ON`, and run:
238 |
239 | ``` shell
240 | $ make -C build test
241 | ```
242 |
243 | ### Running the python test suite
244 |
245 | ``` shell
246 | $ (cd build/faiss/python && python setup.py build)
247 | $ PYTHONPATH="$(ls -d ./build/faiss/python/build/lib*/)" pytest tests/test_*.py
248 | ```
249 |
250 | ### Basic example
251 |
252 | A basic usage example is available in
253 | [`demos/demo_ivfpq_indexing.cpp`](https://github.com/facebookresearch/faiss/blob/main/demos/demo_ivfpq_indexing.cpp).
254 |
255 | It creates a small index, stores it and performs some searches. A normal runtime
256 | is around 20s. With a fast machine and Intel MKL's BLAS it runs in 2.5s.
257 |
258 | It can be built with
259 | ``` shell
260 | $ make -C build demo_ivfpq_indexing
261 | ```
262 | and subsequently ran with
263 | ``` shell
264 | $ ./build/demos/demo_ivfpq_indexing
265 | ```
266 |
267 | ### Basic GPU example
268 |
269 | ``` shell
270 | $ make -C build demo_ivfpq_indexing_gpu
271 | $ ./build/demos/demo_ivfpq_indexing_gpu
272 | ```
273 |
274 | This produce the GPU code equivalent to the CPU `demo_ivfpq_indexing`. It also
275 | shows how to translate indexes from/to a GPU.
276 |
277 | ### A real-life benchmark
278 |
279 | A longer example runs and evaluates Faiss on the SIFT1M dataset. To run it,
280 | please download the ANN_SIFT1M dataset from http://corpus-texmex.irisa.fr/
281 | and unzip it to the subdirectory `sift1M` at the root of the source
282 | directory for this repository.
283 |
284 | Then compile and run the following (after ensuring you have installed faiss):
285 |
286 | ``` shell
287 | $ make -C build demo_sift1M
288 | $ ./build/demos/demo_sift1M
289 | ```
290 |
291 | This is a demonstration of the high-level auto-tuning API. You can try
292 | setting a different index_key to find the indexing structure that
293 | gives the best performance.
294 |
295 | ### Real-life test
296 |
297 | The following script extends the demo_sift1M test to several types of
298 | indexes. This must be run from the root of the source directory for this
299 | repository:
300 |
301 | ``` shell
302 | $ mkdir tmp  # graphs of the output will be written here
303 | $ python demos/demo_auto_tune.py
304 | ```
305 |
306 | It will cycle through a few types of indexes and find optimal
307 | operating points. You can play around with the types of indexes.
308 |
309 | ### Real-life test on GPU
310 |
311 | The example above also runs on GPU. Edit `demos/demo_auto_tune.py` at line 100
312 | with the values
313 |
314 | ``` python
315 | keys_to_test = keys_gpu
316 | use_gpu = True
317 | ```
318 |
319 | and you can run
320 | ``` shell
321 | $ python demos/demo_auto_tune.py
322 | ```
323 | to test the GPU code.
324 |


--------------------------------------------------------------------------------
/README.md:
--------------------------------------------------------------------------------
 1 | # Faiss
 2 |
 3 | Faiss is a library for efficient similarity search and clustering of dense vectors. It contains algorithms that search in sets of vectors of any size, up to ones that possibly do not fit in RAM. It also contains supporting code for evaluation and parameter tuning. Faiss is written in C++ with complete wrappers for Python/numpy. Some of the most useful algorithms are implemented on the GPU. It is developed primarily at Meta's [Fundamental AI Research](https://ai.facebook.com/) group.
 4 |
 5 | ## News
 6 |
 7 | See [CHANGELOG.md](CHANGELOG.md) for detailed information about latest features.
 8 |
 9 | ## Introduction
10 |
11 | Faiss contains several methods for similarity search. It assumes that the instances are represented as vectors and are identified by an integer, and that the vectors can be compared with L2 (Euclidean) distances or dot products. Vectors that are similar to a query vector are those that have the lowest L2 distance or the highest dot product with the query vector. It also supports cosine similarity, since this is a dot product on normalized vectors.
12 |
13 | Some of the methods, like those based on binary vectors and compact quantization codes, solely use a compressed representation of the vectors and do not require to keep the original vectors. This generally comes at the cost of a less precise search but these methods can scale to billions of vectors in main memory on a single server. Other methods, like HNSW and NSG add an indexing structure on top of the raw vectors to make searching more efficient.
14 |
15 | The GPU implementation can accept input from either CPU or GPU memory. On a server with GPUs, the GPU indexes can be used a drop-in replacement for the CPU indexes (e.g., replace `IndexFlatL2` with `GpuIndexFlatL2`) and copies to/from GPU memory are handled automatically. Results will be faster however if both input and output remain resident on the GPU. Both single and multi-GPU usage is supported.
16 |
17 | ## Installing
18 |
19 | Faiss comes with precompiled libraries for Anaconda in Python, see [faiss-cpu](https://anaconda.org/pytorch/faiss-cpu), [faiss-gpu](https://anaconda.org/pytorch/faiss-gpu) and [faiss-gpu-cuvs](https://anaconda.org/pytorch/faiss-gpu-cuvs). The library is mostly implemented in C++, the only dependency is a [BLAS](https://en.wikipedia.org/wiki/Basic_Linear_Algebra_Subprograms) implementation. Optional GPU support is provided via CUDA or AMD ROCm, and the Python interface is also optional. The backend GPU implementations of NVIDIA [cuVS](https://github.com/rapidsai/cuvs) can also be enabled optionally. It compiles with cmake. See [INSTALL.md](INSTALL.md) for details.
20 |
21 | ## How Faiss works
22 |
23 | Faiss is built around an index type that stores a set of vectors, and provides a function to search in them with L2 and/or dot product vector comparison. Some index types are simple baselines, such as exact search. Most of the available indexing structures correspond to various trade-offs with respect to
24 |
25 | - search time
26 | - search quality
27 | - memory used per index vector
28 | - training time
29 | - adding time
30 | - need for external data for unsupervised training
31 |
32 | The optional GPU implementation provides what is likely (as of March 2017) the fastest exact and approximate (compressed-domain) nearest neighbor search implementation for high-dimensional vectors, fastest Lloyd's k-means, and fastest small k-selection algorithm known. [The implementation is detailed here](https://arxiv.org/abs/1702.08734).
33 |
34 | ## Full documentation of Faiss
35 |
36 | The following are entry points for documentation:
37 |
38 | - the full documentation can be found on the [wiki page](http://github.com/facebookresearch/faiss/wiki), including a [tutorial](https://github.com/facebookresearch/faiss/wiki/Getting-started), a [FAQ](https://github.com/facebookresearch/faiss/wiki/FAQ) and a [troubleshooting section](https://github.com/facebookresearch/faiss/wiki/Troubleshooting)
39 | - the [doxygen documentation](https://faiss.ai/) gives per-class information extracted from code comments
40 | - to reproduce results from our research papers, [Polysemous codes](https://arxiv.org/abs/1609.01882) and [Billion-scale similarity search with GPUs](https://arxiv.org/abs/1702.08734), refer to the [benchmarks README](benchs/README.md). For [
41 | Link and code: Fast indexing with graphs and compact regression codes](https://arxiv.org/abs/1804.09996), see the [link_and_code README](benchs/link_and_code)
42 |
43 | ## Authors
44 |
45 | The main authors of Faiss are:
46 | - [Hervé Jégou](https://github.com/jegou) initiated the Faiss project and wrote its first implementation
47 | - [Matthijs Douze](https://github.com/mdouze) implemented most of the CPU Faiss
48 | - [Jeff Johnson](https://github.com/wickedfoo) implemented all of the GPU Faiss
49 | - [Lucas Hosseini](https://github.com/beauby) implemented the binary indexes and the build system
50 | - [Chengqi Deng](https://github.com/KinglittleQ) implemented NSG, NNdescent and much of the additive quantization code.
51 | - [Alexandr Guzhva](https://github.com/alexanderguzhva) many optimizations: SIMD, memory allocation and layout, fast decoding kernels for vector codecs, etc.
52 | - [Gergely Szilvasy](https://github.com/algoriddle) build system, benchmarking framework.
53 |
54 | ## Reference
55 |
56 | References to cite when you use Faiss in a research paper:
57 | ```
58 | @article{douze2024faiss,
59 |       title={The Faiss library},
60 |       author={Matthijs Douze and Alexandr Guzhva and Chengqi Deng and Jeff Johnson and Gergely Szilvasy and Pierre-Emmanuel Mazaré and Maria Lomeli and Lucas Hosseini and Hervé Jégou},
61 |       year={2024},
62 |       eprint={2401.08281},
63 |       archivePrefix={arXiv},
64 |       primaryClass={cs.LG}
65 | }
66 | ```
67 | For the GPU version of Faiss, please cite:
68 | ```
69 | @article{johnson2019billion,
70 |   title={Billion-scale similarity search with {GPUs}},
71 |   author={Johnson, Jeff and Douze, Matthijs and J{\'e}gou, Herv{\'e}},
72 |   journal={IEEE Transactions on Big Data},
73 |   volume={7},
74 |   number={3},
75 |   pages={535--547},
76 |   year={2019},
77 |   publisher={IEEE}
78 | }
79 | ```
80 |
81 | ## Join the Faiss community
82 |
83 | For public discussion of Faiss or for questions, visit https://github.com/facebookresearch/faiss/discussions.
84 |
85 | We monitor the [issues page](http://github.com/facebookresearch/faiss/issues) of the repository.
86 | You can report bugs, ask questions, etc.
87 |
88 | ## Legal
89 |
90 | Faiss is MIT-licensed, refer to the [LICENSE file](https://github.com/facebookresearch/faiss/blob/main/LICENSE) in the top level directory.
91 |
92 | Copyright © Meta Platforms, Inc.
93 |


--------------------------------------------------------------------------------
/benchs/README.md:
--------------------------------------------------------------------------------
  1 |
  2 | # Benchmarking scripts
  3 |
  4 | This directory contains benchmarking scripts that can reproduce the
  5 | numbers reported in the two papers
  6 |
  7 | ```
  8 | @inproceedings{DJP16,
  9 |   Author = {Douze, Matthijs and J{\'e}gou, Herv{\'e} and Perronnin, Florent},
 10 |   Booktitle = "ECCV",
 11 |   Organization = {Springer},
 12 |   Title = {Polysemous codes},
 13 |   Year = {2016}
 14 | }
 15 | ```
 16 | and
 17 |
 18 | ```
 19 | @inproceedings{JDJ17,
 20 |    Author = {Jeff Johnson and Matthijs Douze and Herv{\'e} J{\'e}gou},
 21 |    journal= {arXiv:1702.08734},,
 22 |    Title = {Billion-scale similarity search with GPUs},
 23 |    Year = {2017},
 24 | }
 25 | ```
 26 |
 27 | Note that the numbers (especially timings) change slightly due to changes in the implementation, different machines, etc.
 28 |
 29 | The scripts are self-contained. They depend only on Faiss and external training data that should be stored in sub-directories.
 30 |
 31 | ## SIFT1M experiments
 32 |
 33 | The script [`bench_polysemous_sift1m.py`](bench_polysemous_sift1m.py) reproduces the numbers in
 34 | Figure 3 from the "Polysemous" paper.
 35 |
 36 | ### Getting SIFT1M
 37 |
 38 | To run it, please download the ANN_SIFT1M dataset from
 39 |
 40 | http://corpus-texmex.irisa.fr/
 41 |
 42 | and unzip it to the subdirectory sift1M.
 43 |
 44 | ### Result
 45 |
 46 | The output looks like:
 47 |
 48 | ```
 49 | PQ training on 100000 points, remains 0 points: training polysemous on centroids
 50 | add vectors to index
 51 | PQ baseline        7.517 ms per query, R@1 0.4474
 52 | Polysemous 64      9.875 ms per query, R@1 0.4474
 53 | Polysemous 62      8.358 ms per query, R@1 0.4474
 54 | Polysemous 58      5.531 ms per query, R@1 0.4474
 55 | Polysemous 54      3.420 ms per query, R@1 0.4478
 56 | Polysemous 50      2.182 ms per query, R@1 0.4475
 57 | Polysemous 46      1.621 ms per query, R@1 0.4408
 58 | Polysemous 42      1.448 ms per query, R@1 0.4174
 59 | Polysemous 38      1.331 ms per query, R@1 0.3563
 60 | Polysemous 34      1.334 ms per query, R@1 0.2661
 61 | Polysemous 30      1.272 ms per query, R@1 0.1794
 62 | ```
 63 |
 64 |
 65 | ## Experiments on 1B elements dataset
 66 |
 67 | The script [`bench_polysemous_1bn.py`](bench_polysemous_1bn.py) reproduces a few experiments on
 68 | two datasets of size 1B from the Polysemous codes" paper.
 69 |
 70 |
 71 | ### Getting BIGANN
 72 |
 73 | Download the four files of ANN_SIFT1B from
 74 | http://corpus-texmex.irisa.fr/ to subdirectory bigann/
 75 |
 76 | ### Getting Deep1B
 77 |
 78 | The ground-truth and queries are available here
 79 |
 80 | https://yadi.sk/d/11eDCm7Dsn9GA
 81 |
 82 | For the learning and database vectors, use the script
 83 |
 84 | https://github.com/arbabenko/GNOIMI/blob/master/downloadDeep1B.py
 85 |
 86 | to download the data to subdirectory deep1b/, then concatenate the
 87 | database files to base.fvecs and the training files to learn.fvecs
 88 |
 89 | ### Running the experiments
 90 |
 91 | These experiments are quite long. To support resuming, the script
 92 | stores the result of training to a temporary directory, `/tmp/bench_polysemous`.
 93 |
 94 | The script `bench_polysemous_1bn.py` takes at least two arguments:
 95 |
 96 | - the dataset name: SIFT1000M (aka SIFT1B, aka BIGANN) or Deep1B. SIFT1M, SIFT2M,... are also supported to make subsets of for small experiments (note that SIFT1M as a subset of SIFT1B is not the same as the SIFT1M above)
 97 |
 98 | - the type of index to build, which should be a valid [index_factory key](https://github.com/facebookresearch/faiss/wiki/High-level-interface-and-auto-tuning#index-factory) (see below for examples)
 99 |
100 | - the remaining arguments are parsed as search-time parameters.
101 |
102 | ### Experiments of Table 2
103 |
104 | The `IMI*+PolyD+ADC` results in Table 2 can be reproduced with (for 16 bytes):
105 |
106 | ```
107 | python bench_polysemous_1bn.par SIFT1000M IMI2x12,PQ16 nprobe=16,max_codes={10000,30000},ht={44..54}
108 | ```
109 |
110 | Training takes about 2 minutes and adding vectors to the dataset
111 | takes 3.1 h. These operations are multithreaded. Note that in the command
112 | above, we use bash's [brace expansion](https://www.gnu.org/software/bash/manual/html_node/Brace-Expansion.html) to set a grid of parameters.
113 |
114 | The search is *not* multithreaded, and the output looks like:
115 |
116 | ```
117 |                                         R@1    R@10   R@100     time    %pass
118 | nprobe=16,max_codes=10000,ht=44         0.1779 0.2994 0.3139    0.194   12.45
119 | nprobe=16,max_codes=10000,ht=45         0.1859 0.3183 0.3339    0.197   14.24
120 | nprobe=16,max_codes=10000,ht=46         0.1930 0.3366 0.3543    0.202   16.22
121 | nprobe=16,max_codes=10000,ht=47         0.1993 0.3550 0.3745    0.209   18.39
122 | nprobe=16,max_codes=10000,ht=48         0.2033 0.3694 0.3917    0.640   20.77
123 | nprobe=16,max_codes=10000,ht=49         0.2070 0.3839 0.4077    0.229   23.36
124 | nprobe=16,max_codes=10000,ht=50         0.2101 0.3949 0.4205    0.232   26.17
125 | nprobe=16,max_codes=10000,ht=51         0.2120 0.4042 0.4310    0.239   29.21
126 | nprobe=16,max_codes=10000,ht=52         0.2134 0.4113 0.4402    0.245   32.47
127 | nprobe=16,max_codes=10000,ht=53         0.2157 0.4184 0.4482    0.250   35.96
128 | nprobe=16,max_codes=10000,ht=54         0.2170 0.4240 0.4546    0.256   39.66
129 | nprobe=16,max_codes=30000,ht=44         0.1882 0.3327 0.3555    0.226   11.29
130 | nprobe=16,max_codes=30000,ht=45         0.1964 0.3525 0.3771    0.231   13.05
131 | nprobe=16,max_codes=30000,ht=46         0.2039 0.3713 0.3987    0.236   15.01
132 | nprobe=16,max_codes=30000,ht=47         0.2103 0.3907 0.4202    0.245   17.19
133 | nprobe=16,max_codes=30000,ht=48         0.2145 0.4055 0.4384    0.251   19.60
134 | nprobe=16,max_codes=30000,ht=49         0.2179 0.4198 0.4550    0.257   22.25
135 | nprobe=16,max_codes=30000,ht=50         0.2208 0.4305 0.4681    0.268   25.15
136 | nprobe=16,max_codes=30000,ht=51         0.2227 0.4402 0.4791    0.275   28.30
137 | nprobe=16,max_codes=30000,ht=52         0.2241 0.4473 0.4884    0.284   31.70
138 | nprobe=16,max_codes=30000,ht=53         0.2265 0.4544 0.4965    0.294   35.34
139 | nprobe=16,max_codes=30000,ht=54         0.2278 0.4601 0.5031    0.303   39.20
140 | ```
141 |
142 | The result reported in table 2 is the one for which the %pass (percentage of code comparisons that pass the Hamming check) is around 20%, which occurs for Hamming threshold `ht=48`.
143 |
144 | The 8-byte results can be reproduced with the factory key `IMI2x12,PQ8`
145 |
146 | ### Experiments of the appendix
147 |
148 | The experiments in the appendix are only in the ArXiv version of the paper (table 3).
149 |
150 | ```
151 | python bench_polysemous_1bn.py SIFT1000M OPQ8_64,IMI2x13,PQ8 nprobe={1,2,4,8,16,32,64,128},ht={20,24,26,28,30}
152 |
153 |                	R@1    R@10   R@100     time    %pass
154 | nprobe=1,ht=20 	0.0351 0.0616 0.0751    0.158   19.01
155 | ...
156 | nprobe=32,ht=28 	0.1256 0.3563 0.5026    0.561   52.61
157 | ...
158 | ```
159 | Here again the runs are not exactly the same but the original result was obtained from nprobe=32,ht=28.
160 |
161 | For Deep1B, we used a simple version of [auto-tuning](https://github.com/facebookresearch/faiss/wiki/High-level-interface-and-auto-tuning/_edit#auto-tuning-the-runtime-parameters) to sweep through the set of operating points:
162 |
163 | ```
164 | python bench_polysemous_1bn.py Deep1B OPQ20_80,IMI2x14,PQ20 autotune
165 | ...
166 | Done in 4067.555 s, available OPs:
167 | Parameters                                1-R@1     time
168 |                                           0.0000    0.000
169 | nprobe=1,ht=22,max_codes=256              0.0215    3.115
170 | nprobe=1,ht=30,max_codes=256              0.0381    3.120
171 | ...
172 | nprobe=512,ht=68,max_codes=524288         0.4478   36.903
173 | nprobe=1024,ht=80,max_codes=131072        0.4557   46.363
174 | nprobe=1024,ht=78,max_codes=262144        0.4616   61.939
175 | ...
176 | ```
177 | The original results were obtained with `nprobe=1024,ht=66,max_codes=262144`.
178 |
179 |
180 | ## GPU experiments
181 |
182 | The benchmarks below run 1 or 4 Titan X GPUs and reproduce the results of the "GPU paper". They are also a good starting point on how to use GPU Faiss.
183 |
184 | ### Search on SIFT1M
185 |
186 | See above on how to get SIFT1M into subdirectory sift1M/. The script [`bench_gpu_sift1m.py`](bench_gpu_sift1m.py) reproduces the "exact k-NN time" plot in the ArXiv paper, and the SIFT1M numbers.
187 |
188 | The output is:
189 | ```
190 | ============ Exact search
191 | add vectors to index
192 | warmup
193 | benchmark
194 | k=1 0.715 s, R@1 0.9914
195 | k=2 0.729 s, R@1 0.9935
196 | k=4 0.731 s, R@1 0.9935
197 | k=8 0.732 s, R@1 0.9935
198 | k=16 0.742 s, R@1 0.9935
199 | k=32 0.737 s, R@1 0.9935
200 | k=64 0.753 s, R@1 0.9935
201 | k=128 0.761 s, R@1 0.9935
202 | k=256 0.799 s, R@1 0.9935
203 | k=512 0.975 s, R@1 0.9935
204 | k=1024 1.424 s, R@1 0.9935
205 | ============ Approximate search
206 | train
207 | WARNING clustering 100000 points to 4096 centroids: please provide at least 159744 training points
208 | add vectors to index
209 | WARN: increase temp memory to avoid cudaMalloc, or decrease query/add size (alloc 256000000 B, highwater 256000000 B)
210 | warmup
211 | benchmark
212 | nprobe=   1 0.043 s recalls= 0.3909 0.4312 0.4312
213 | nprobe=   2 0.040 s recalls= 0.5041 0.5636 0.5636
214 | nprobe=   4 0.048 s recalls= 0.6048 0.6897 0.6897
215 | nprobe=   8 0.064 s recalls= 0.6879 0.8028 0.8028
216 | nprobe=  16 0.088 s recalls= 0.7534 0.8940 0.8940
217 | nprobe=  32 0.134 s recalls= 0.7957 0.9549 0.9550
218 | nprobe=  64 0.224 s recalls= 0.8125 0.9833 0.9834
219 | nprobe= 128 0.395 s recalls= 0.8205 0.9953 0.9954
220 | nprobe= 256 0.717 s recalls= 0.8227 0.9993 0.9994
221 | nprobe= 512 1.348 s recalls= 0.8228 0.9999 1.0000
222 | ```
223 | The run produces two warnings:
224 |
225 | - the clustering complains that it does not have enough training data, there is not much we can do about this.
226 |
227 | - the add() function complains that there is an inefficient memory allocation, but this is a concern only when it happens often, and we are not benchmarking the add time anyways.
228 |
229 | To index small datasets, it is more efficient to use a `GpuIVFFlat`, which just stores the full vectors in the inverted lists. We did not mention this in the the paper because it is not as scalable. To experiment with this setting, change the `index_factory` string from "IVF4096,PQ64" to "IVF16384,Flat". This gives:
230 |
231 | ```
232 | nprobe=   1 0.025 s recalls= 0.4084 0.4105 0.4105
233 | nprobe=   2 0.033 s recalls= 0.5235 0.5264 0.5264
234 | nprobe=   4 0.033 s recalls= 0.6332 0.6367 0.6367
235 | nprobe=   8 0.040 s recalls= 0.7358 0.7403 0.7403
236 | nprobe=  16 0.049 s recalls= 0.8273 0.8324 0.8324
237 | nprobe=  32 0.068 s recalls= 0.8957 0.9024 0.9024
238 | nprobe=  64 0.104 s recalls= 0.9477 0.9549 0.9549
239 | nprobe= 128 0.174 s recalls= 0.9760 0.9837 0.9837
240 | nprobe= 256 0.299 s recalls= 0.9866 0.9944 0.9944
241 | nprobe= 512 0.527 s recalls= 0.9907 0.9987 0.9987
242 | ```
243 |
244 | ### Clustering on MNIST8m
245 |
246 | To get the "infinite MNIST dataset", follow the instructions on [Léon Bottou's website](http://leon.bottou.org/projects/infimnist). The script assumes the file `mnist8m-patterns-idx3-ubyte` is in subdirectory `mnist8m`
247 |
248 | The script [`kmeans_mnist.py`](kmeans_mnist.py) produces the following output:
249 |
250 | ```
251 | python kmeans_mnist.py 1 256
252 | ...
253 | Clustering 8100000 points in 784D to 256 clusters, redo 1 times, 20 iterations
254 |   Preprocessing in 7.94526 s
255 |   Iteration 19 (131.697 s, search 114.78 s): objective=1.44881e+13 imbalance=1.05963 nsplit=0
256 | final objective: 1.449e+13
257 | total runtime: 140.615 s
258 | ```
259 |
260 | ### search on SIFT1B
261 |
262 | The script [`bench_gpu_1bn.py`](bench_gpu_1bn.py) runs multi-gpu searches on the two 1-billion vector datasets we considered. It is more complex than the previous scripts, because it supports many search options and decomposes the dataset build process in Python to exploit the best possible CPU/GPU parallelism and GPU distribution.
263 |
264 | Even on multiple GPUs, building the 1B datasets can last several hours. It is often a good idea to validate that everything is working fine on smaller datasets like SIFT1M, SIFT2M, etc.
265 |
266 | The search results on SIFT1B in the "GPU paper" can be obtained with
267 |
268 | <!-- see P57124181 -->
269 |
270 | ```
271 | python bench_gpu_1bn.py SIFT1000M OPQ8_32,IVF262144,PQ8 -nnn 10 -ngpu 1 -tempmem $[1536*1024*1024]
272 | ...
273 | 0/10000 (0.024 s)      probe=1  : 0.161 s 1-R@1: 0.0752 1-R@10: 0.1924
274 | 0/10000 (0.005 s)      probe=2  : 0.150 s 1-R@1: 0.0964 1-R@10: 0.2693
275 | 0/10000 (0.005 s)      probe=4  : 0.153 s 1-R@1: 0.1102 1-R@10: 0.3328
276 | 0/10000 (0.005 s)      probe=8  : 0.170 s 1-R@1: 0.1220 1-R@10: 0.3827
277 | 0/10000 (0.005 s)      probe=16 : 0.196 s 1-R@1: 0.1290 1-R@10: 0.4151
278 | 0/10000 (0.006 s)      probe=32 : 0.244 s 1-R@1: 0.1314 1-R@10: 0.4345
279 | 0/10000 (0.006 s)      probe=64 : 0.353 s 1-R@1: 0.1332 1-R@10: 0.4461
280 | 0/10000 (0.005 s)      probe=128: 0.587 s 1-R@1: 0.1341 1-R@10: 0.4502
281 | 0/10000 (0.006 s)      probe=256: 1.160 s 1-R@1: 0.1342 1-R@10: 0.4511
282 | ```
283 |
284 | We use the `-tempmem` option to reduce the temporary memory allocation to 1.5G, otherwise the dataset does not fit in GPU memory
285 |
286 | ### search on Deep1B
287 |
288 | The same script generates the GPU search results on Deep1B.
289 |
290 | ```
291 | python bench_gpu_1bn.py  Deep1B OPQ20_80,IVF262144,PQ20 -nnn 10 -R 2 -ngpu 4 -altadd -noptables -tempmem $[1024*1024*1024]
292 | ...
293 |
294 | 0/10000 (0.115 s)      probe=1  : 0.239 s 1-R@1: 0.2387 1-R@10: 0.3420
295 | 0/10000 (0.006 s)      probe=2  : 0.103 s 1-R@1: 0.3110 1-R@10: 0.4623
296 | 0/10000 (0.005 s)      probe=4  : 0.105 s 1-R@1: 0.3772 1-R@10: 0.5862
297 | 0/10000 (0.005 s)      probe=8  : 0.116 s 1-R@1: 0.4235 1-R@10: 0.6889
298 | 0/10000 (0.005 s)      probe=16 : 0.133 s 1-R@1: 0.4517 1-R@10: 0.7693
299 | 0/10000 (0.005 s)      probe=32 : 0.168 s 1-R@1: 0.4713 1-R@10: 0.8281
300 | 0/10000 (0.005 s)      probe=64 : 0.238 s 1-R@1: 0.4841 1-R@10: 0.8649
301 | 0/10000 (0.007 s)      probe=128: 0.384 s 1-R@1: 0.4900 1-R@10: 0.8816
302 | 0/10000 (0.005 s)      probe=256: 0.736 s 1-R@1: 0.4933 1-R@10: 0.8912
303 | ```
304 |
305 | Here we are a bit tight on memory so we disable precomputed tables (`-noptables`) and restrict the amount of temporary memory. The `-altadd` option avoids GPU memory overflows during add.
306 |
307 |
308 | ### knn-graph on Deep1B
309 |
310 | The same script generates the KNN-graph on Deep1B. Note that the inverted file from above will not be re-used because the training sets are different. For the knngraph, the script will first do a pass over the whole dataset to compute the ground-truth knn for a subset of 10k nodes, for evaluation.
311 |
312 | ```
313 | python bench_gpu_1bn.py Deep1B OPQ20_80,IVF262144,PQ20 -nnn 10 -altadd -knngraph  -R 2 -noptables -tempmem $[1<<30] -ngpu 4
314 | ...
315 | CPU index contains 1000000000 vectors, move to GPU
316 | Copy CPU index to 2 sharded GPU indexes
317 |    dispatch to GPUs 0:2
318 | IndexShards shard 0 indices 0:500000000
319 |   IndexIVFPQ size 500000000 -> GpuIndexIVFPQ indicesOptions=0 usePrecomputed=0 useFloat16=0 reserveVecs=0
320 | IndexShards shard 1 indices 500000000:1000000000
321 |   IndexIVFPQ size 500000000 -> GpuIndexIVFPQ indicesOptions=0 usePrecomputed=0 useFloat16=0 reserveVecs=0
322 |    dispatch to GPUs 2:4
323 | IndexShards shard 0 indices 0:500000000
324 |   IndexIVFPQ size 500000000 -> GpuIndexIVFPQ indicesOptions=0 usePrecomputed=0 useFloat16=0 reserveVecs=0
325 | IndexShards shard 1 indices 500000000:1000000000
326 |   IndexIVFPQ size 500000000 -> GpuIndexIVFPQ indicesOptions=0 usePrecomputed=0 useFloat16=0 reserveVecs=0
327 | move to GPU done in 151.535 s
328 | search...
329 | 999997440/1000000000 (8389.961 s, 0.3379)      probe=1  : 8389.990 s rank-10 intersection results: 0.3379
330 | 999997440/1000000000 (9205.934 s, 0.4079)      probe=2  : 9205.966 s rank-10 intersection results: 0.4079
331 | 999997440/1000000000 (9741.095 s, 0.4722)      probe=4  : 9741.128 s rank-10 intersection results: 0.4722
332 | 999997440/1000000000 (10830.420 s, 0.5256)      probe=8  : 10830.455 s rank-10 intersection results: 0.5256
333 | 999997440/1000000000 (12531.716 s, 0.5603)      probe=16 : 12531.758 s rank-10 intersection results: 0.5603
334 | 999997440/1000000000 (15922.519 s, 0.5825)      probe=32 : 15922.571 s rank-10 intersection results: 0.5825
335 | 999997440/1000000000 (22774.153 s, 0.5950)      probe=64 : 22774.220 s rank-10 intersection results: 0.5950
336 | 999997440/1000000000 (36717.207 s, 0.6015)      probe=128: 36717.309 s rank-10 intersection results: 0.6015
337 | 999997440/1000000000 (70616.392 s, 0.6047)      probe=256: 70616.581 s rank-10 intersection results: 0.6047
338 | ```
339 |
340 | # Additional benchmarks
341 |
342 | This directory also contains certain additional benchmarks (and serve as an additional source of examples of how to use the Faiss code).
343 | Certain tests / benchmarks might be outdated.
344 |
345 | * bench_6bit_codec.cpp - tests vector codecs for SQ6 quantization on a synthetic dataset
346 | * bench_cppcontrib_sa_decode.cpp - benchmarks specialized kernels for vector codecs for PQ, IVFPQ and Resudial+PQ on a synthetic dataset
347 | * bench_for_interrupt.py - evaluates the impact of the interrupt callback handler (which can be triggered from Python code)
348 | * bench_hamming_computer.cpp - specialized implementations for Hamming distance computations
349 | * bench_heap_replace.cpp - benchmarks different implementations of certain calls for a Heap data structure
350 | * bench_hnsw.py - benchmarks HNSW in combination with other ones for SIFT1M dataset
351 | * bench_index_flat.py - benchmarks IndexFlatL2 on a synthetic dataset
352 | * bench_index_pq.py - benchmarks PQ on SIFT1M dataset
353 | * bench_ivf_fastscan_single_query.py - benchmarks a single query for different nprobe levels for IVF{nlist},PQ{M}x4fs on BIGANN dataset
354 | * bench_ivf_fastscan.py - compares IVF{nlist},PQ{M}x4fs against other indices on SIFT1M dataset
355 | * bench_ivf_selector.cpp - checks the possible overhead when using faiss::IDSelectorAll interface
356 | * bench_pairwise_distances.py - benchmarks pairwise distance computation between two synthetic datasets
357 | * bench_partition.py - benchmarks partitioning functions
358 | * bench_pq_tables.py - benchmarks ProductQuantizer.compute_inner_prod_tables() and ProductQuantizer.compute_distance_tables() calls
359 | * bench_quantizer.py - benchmarks various quantizers for SIFT1M, Deep1B, BigANN datasets
360 | * bench_scalar_quantizer.py - benchmarks IVF+SQ on a Sift1M dataset
361 | * bench_vector_ops.py - benchmarks dot product and distances computations on a synthetic dataset
362 |


--------------------------------------------------------------------------------
/benchs/bench_all_ivf/README.md:
--------------------------------------------------------------------------------
 1 | # Benchmark of IVF variants
 2 |
 3 | This is a benchmark of IVF index variants, looking at compression vs. speed vs. accuracy.
 4 | The results are in [this wiki chapter](https://github.com/facebookresearch/faiss/wiki/Indexing-1G-vectors)
 5 |
 6 |
 7 | The code is organized as:
 8 |
 9 | - `datasets.py`: code to access the datafiles, compute the ground-truth and report accuracies
10 |
11 | - `bench_all_ivf.py`: evaluate one type of inverted file
12 |
13 | - `run_on_cluster_generic.bash`: call `bench_all_ivf.py` for all tested types of indices.
14 | Since the number of experiments is quite large the script is structured so that the benchmark can be run on a cluster.
15 |
16 | - `parse_bench_all_ivf.py`: make nice tradeoff plots from all the results.
17 |
18 | The code depends on Faiss and can use 1 to 8 GPUs to do the k-means clustering for large vocabularies.
19 |
20 | It was run in October 2018 for the results in the wiki.
21 |


--------------------------------------------------------------------------------
/benchs/distributed_ondisk/README.md:
--------------------------------------------------------------------------------
  1 | # Distributed on-disk index for 1T-scale datasets
  2 |
  3 | This is code corresponding to the description in [Indexing 1T vectors](https://github.com/facebookresearch/faiss/wiki/Indexing-1T-vectors).
  4 | All the code is in python 3 (and not compatible with Python 2).
  5 | The current code uses the Deep1B dataset for demonstration purposes, but can scale to 1000x larger.
  6 | To run it, download the Deep1B dataset as explained [here](../#getting-deep1b), and edit paths to the dataset in the scripts.
  7 |
  8 | The cluster commands are written for the Slurm batch scheduling system.
  9 | Hopefully, changing to another type of scheduler should be quite straightforward.
 10 |
 11 | ## Distributed k-means
 12 |
 13 | To cluster 500M vectors to 10M centroids, it is useful to have a distributed k-means implementation.
 14 | The distribution simply consists in splitting the training vectors across machines (servers) and have them do the assignment.
 15 | The master/client then synthesizes the results and updates the centroids.
 16 |
 17 | The distributed k-means implementation here is based on 3 files:
 18 |
 19 | - [`distributed_kmeans.py`](distributed_kmeans.py) contains the k-means implementation.
 20 | The main loop of k-means is re-implemented in python but follows closely the Faiss C++ implementation, and should not be significantly less efficient.
 21 | It relies on a `DatasetAssign` object that does the assignment to centroids, which is the bulk of the computation.
 22 | The object can be a Faiss CPU index, a GPU index or a set of remote GPU or CPU indexes.
 23 |
 24 | - [`run_on_cluster.bash`](run_on_cluster.bash) contains the shell code to run the distributed k-means on a cluster.
 25 |
 26 | The distributed k-means works with a Python install that contains faiss and scipy (for sparse matrices).
 27 | It clusters the training data of Deep1B, this can be changed easily to any file in fvecs, bvecs or npy format that contains the training set.
 28 | The training vectors may be too large to fit in RAM, but they are memory-mapped so that should not be a problem.
 29 | The file is also assumed to be accessible from all server machines with eg. a distributed file system.
 30 |
 31 | ### Local tests
 32 |
 33 | Edit `distributed_kmeans.py` to point `testdata` to your local copy of the dataset.
 34 |
 35 | Then, 4 levels of sanity check can be run:
 36 | ```bash
 37 | # reference Faiss C++ run
 38 | python distributed_kmeans.py --test 0
 39 | # using the Python implementation
 40 | python distributed_kmeans.py --test 1
 41 | # use the dispatch object (on local datasets)
 42 | python distributed_kmeans.py --test 2
 43 | # same, with GPUs
 44 | python distributed_kmeans.py --test 3
 45 | ```
 46 | The output should look like [This gist](https://gist.github.com/mdouze/ffa01fe666a9325761266fe55ead72ad).
 47 |
 48 | ### Distributed sanity check
 49 |
 50 | To run the distributed k-means, `distributed_kmeans.py` has to be run both on the servers (`--server` option) and client sides (`--client` option).
 51 | Edit the top of `run_on_cluster.bash` to set the path of the data to cluster.
 52 |
 53 | Sanity checks can be run with
 54 | ```bash
 55 | # non distributed baseline
 56 | bash run_on_cluster.bash test_kmeans_0
 57 | # using all the machine's GPUs
 58 | bash run_on_cluster.bash test_kmeans_1
 59 | # distributed run, with one local server per GPU
 60 | bash run_on_cluster.bash test_kmeans_2
 61 | ```
 62 | The test `test_kmeans_2` simulates a distributed run on a single machine by starting one server process per GPU and connecting to the servers via the rpc protocol.
 63 | The output should look like [this gist](https://gist.github.com/mdouze/5b2dc69b74579ecff04e1686a277d32e).
 64 |
 65 |
 66 |
 67 | ### Distributed run
 68 |
 69 | The way the script can be distributed depends on the cluster's scheduling system.
 70 | Here we use Slurm, but it should be relatively easy to adapt to any scheduler that can allocate a set of machines and start the same executable on all of them.
 71 |
 72 | The command
 73 | ```bash
 74 | bash run_on_cluster.bash slurm_distributed_kmeans
 75 | ```
 76 | asks SLURM for 5 machines with 4 GPUs each with the `srun` command.
 77 | All 5 machines run the script with the `slurm_within_kmeans_server` option.
 78 | They determine the number of servers and their own server id via the `SLURM_NPROCS` and `SLURM_PROCID` environment variables.
 79 |
 80 | All machines start `distributed_kmeans.py` in server mode for the slice of the dataset they are responsible for.
 81 |
 82 | In addition, the machine #0 also starts the client.
 83 | The client knows who are the other servers via the variable `SLURM_JOB_NODELIST`.
 84 | It connects to all clients and performs the clustering.
 85 |
 86 | The output should look like [this gist](https://gist.github.com/mdouze/8d25e89fb4af5093057cae0f917da6cd).
 87 |
 88 | ### Run used for deep1B
 89 |
 90 | For the real run, we run the clustering on 50M vectors to 1M centroids.
 91 | This is just a matter of using as many machines / GPUs as possible in setting the output centroids with the `--out filename` option.
 92 | Then run
 93 | ```bash
 94 | bash run_on_cluster.bash deep1b_clustering
 95 | ```
 96 |
 97 | The last lines of output read like:
 98 | ```bash
 99 |   Iteration 19 (898.92 s, search 875.71 s): objective=1.33601e+07 imbalance=1.303 nsplit=0
100 |  0: writing centroids to /checkpoint/matthijs/ondisk_distributed/1M_centroids.npy
101 | ```
102 |
103 | This means that the total training time was 899s, of which 876s were used for computation.
104 | However, the computation includes the I/O overhead to the assignment servers.
105 | In this implementation, the overhead of transmitting the data is non-negligible and so is the centroid computation stage.
106 | This is due to the inefficient Python implementation and the RPC protocol that is not optimized for broadcast / gather (like MPI).
107 | However, it is a simple implementation that should run on most clusters.
108 |
109 | ## Making the trained index
110 |
111 | After the centroids are obtained, an empty trained index must be constructed.
112 | This is done by:
113 |
114 | - applying a pre-processing stage (a random rotation) to balance the dimensions of the vectors. This can be done after clustering, the clusters are just rotated as well.
115 |
116 | - wrapping the centroids into a HNSW index to speed up the CPU-based assignment of vectors
117 |
118 | - training the 6-bit scalar quantizer used to encode the vectors
119 |
120 | This is performed by the script [`make_trained_index.py`](make_trained_index.py).
121 |
122 | ## Building the index by slices
123 |
124 | We call the slices "vslices" as they are vertical slices of the big matrix, see explanation in the wiki section [Split across database partitions](https://github.com/facebookresearch/faiss/wiki/Indexing-1T-vectors#split-across-database-partitions).
125 |
126 | The script [make_index_vslice.py](make_index_vslice.py) makes an index for a subset of the vectors of the input data and stores it as an independent index.
127 | There are 200 slices of 5M vectors each for Deep1B.
128 | It can be run in a brute-force parallel fashion, there is no constraint on ordering.
129 | To run the script in parallel on a slurm cluster, use:
130 | ```bash
131 | bash run_on_cluster.bash make_index_vslices
132 | ```
133 | For a real dataset, the data would be read from a DBMS.
134 | In that case, reading the data and indexing it in parallel is worthwhile because reading is very slow.
135 |
136 | ## Splitting across inverted lists
137 |
138 | The 200 slices need to be merged together.
139 | This is done with the script [merge_to_ondisk.py](merge_to_ondisk.py), that memory maps the 200 vertical slice indexes, extracts a subset of the inverted lists and writes them to a contiguous horizontal slice.
140 | We slice the inverted lists into 50 horizontal slices.
141 | This is run with
142 | ```bash
143 | bash run_on_cluster.bash make_index_hslices
144 | ```
145 |
146 | ## Querying the index
147 |
148 | At this point the index is ready.
149 | The horizontal slices need to be loaded in the right order and combined into an index to be usable.
150 | This is done in the [combined_index.py](combined_index.py) script.
151 | It provides a `CombinedIndexDeep1B` object that contains an index object that can be searched.
152 | To test, run:
153 | ```bash
154 | python combined_index.py
155 | ```
156 | The output should look like:
157 | ```bash
158 | (faiss_1.5.2) matthijs@devfair0144:~/faiss_versions/faiss_1Tcode/faiss/benchs/distributed_ondisk$ python combined_index.py
159 | reading /checkpoint/matthijs/ondisk_distributed//hslices/slice49.faissindex
160 | loading empty index /checkpoint/matthijs/ondisk_distributed/trained.faissindex
161 | replace invlists
162 | loaded index of size  1000000000
163 | nprobe=1 1-recall@1=0.2904 t=12.35s
164 | nnprobe=10 1-recall@1=0.6499 t=17.67s
165 | nprobe=100 1-recall@1=0.8673 t=29.23s
166 | nprobe=1000 1-recall@1=0.9132 t=129.58s
167 | ```
168 | ie. searching is a lot slower than from RAM.
169 |
170 | ## Distributed query
171 |
172 | To reduce the bandwidth required from the machine that does the queries, it is possible to split the search across several search servers.
173 | This way, only the effective results are returned to the main machine.
174 |
175 | The search client and server are implemented in [`search_server.py`](search_server.py).
176 | It can be used as a script to start a search server for `CombinedIndexDeep1B` or as a module to load the clients.
177 |
178 | The search servers can be started with
179 | ```bash
180 | bash run_on_cluster.bash run_search_servers
181 | ```
182 | (adjust to the number of servers that can be used).
183 |
184 | Then an example of search client is [`distributed_query_demo.py`](distributed_query_demo.py).
185 | It connects to the servers and assigns subsets of inverted lists to visit to each of them.
186 |
187 | A typical output is [this gist](https://gist.github.com/mdouze/1585b9854a9a2437d71f2b2c3c05c7c5).
188 | The number in MiB indicates the amount of data that is read from disk to perform the search.
189 | In this case, the scale of the dataset is too small for the distributed search to have much impact, but on datasets > 10x larger, the difference becomes more significant.
190 |
191 | ## Conclusion
192 |
193 | This code contains the core components to make an index that scales up to 1T vectors.
194 | There are a few simplifications wrt. the index that was effectively used in [Indexing 1T vectors](https://github.com/facebookresearch/faiss/wiki/Indexing-1T-vectors).
195 |


--------------------------------------------------------------------------------
/benchs/link_and_code/README.md:
--------------------------------------------------------------------------------
 1 |
 2 |
 3 | README for the link & code implementation
 4 | =========================================
 5 |
 6 | What is this?
 7 | -------------
 8 |
 9 | Link & code is an indexing method that combines HNSW indexing with
10 | compression and exploits the neighborhood structure of the similarity
11 | graph to improve the reconstruction. It is described in
12 |
13 | ```
14 | @inproceedings{link_and_code,
15 |    author = {Matthijs Douze and Alexandre Sablayrolles and Herv\'e J\'egou},
16 |    title = {Link and code: Fast indexing with graphs and compact regression codes},
17 |    booktitle = {CVPR},
18 |    year = {2018}
19 | }
20 | ```
21 |
22 | ArXiV [here](https://arxiv.org/abs/1804.09996)
23 |
24 | The necessary code for this paper was removed from Faiss in version 1.8.0.
25 | For a functioning verinsion, use Faiss 1.7.4.
26 |


--------------------------------------------------------------------------------
/c_api/INSTALL.md:
--------------------------------------------------------------------------------
  1 | Faiss C API
  2 | ===========
  3 |
  4 | Faiss provides a pure C interface, which can subsequently be used either in pure C programs or to produce bindings for programming languages with Foreign Function Interface (FFI) support. Although this is not required for the Python interface, some other programming languages (e.g. Rust and Julia) do not have SWIG support.
  5 |
  6 | Compilation instructions
  7 | ------------------------
  8 |
  9 | The full contents of the pure C API are in the ["c_api"](c_api/) folder.
 10 | Please be sure to follow the instructions on [building the main C++ library](../INSTALL.md#step-1-compiling-the-c-faiss) first.
 11 | Include `-DFAISS_ENABLE_C_API=ON` to the cmake command.
 12 |
 13 | `make -C build`
 14 |
 15 |
 16 | This builds the dynamic library "faiss_c", containing the full implementation of Faiss and the necessary wrappers for the C interface. It does not depend on libfaiss.a or the C++ standard library.
 17 |
 18 | To build the example program, you should run `make -C build example_c` at the top level of
 19 | the faiss repo. The example program will be in `build/c_api/example_c` .
 20 |
 21 | Using the API
 22 | -------------
 23 |
 24 | The C API is composed of:
 25 |
 26 | - A set of C header files comprising the main Faiss interfaces, converted for use in C. Each file follows the format `«name»_c.h`, where `«name»` is the respective name from the C++ API. For example, the file [Index_c.h](./Index_c.h) file corresponds to the base `Index` API. Functions are declared with the `faiss_` prefix (e.g. `faiss_IndexFlat_new`), whereas new types have the `Faiss` prefix (e.g. `FaissIndex`, `FaissMetricType`, ...).
 27 | - A dynamic library, compiled from the sources in the same folder, encloses the implementation of the library and wrapper functions.
 28 |
 29 | The index factory is available via the `faiss_index_factory` function in `AutoTune_c.h`:
 30 |
 31 | ```c
 32 | FaissIndex* index = NULL;
 33 | int c = faiss_index_factory(&index, 64, "Flat", METRIC_L2);
 34 | if (c) {
 35 |     // operation failed
 36 | }
 37 | ```
 38 |
 39 | Most operations that you would find as member functions are available with the format `faiss_«classname»_«member»`.
 40 |
 41 | ```c
 42 | idx_t ntotal = faiss_Index_ntotal(index);
 43 | ```
 44 |
 45 | Since this is C, the index needs to be freed manually in the end:
 46 |
 47 | ```c
 48 | faiss_Index_free(index);
 49 | ```
 50 |
 51 | Error handling is done by examining the error code returned by operations with recoverable errors.
 52 | The code identifies the type of exception that rose from the implementation. Fetching the
 53 | corresponding error message can be done by calling the function `faiss_get_last_error()` from
 54 | `error_c.h`. Getter functions and `free` functions do not return an error code.
 55 |
 56 | ```c
 57 | int c = faiss_Index_add(index, nb, xb);
 58 | if (c) {
 59 |     printf("%s", faiss_get_last_error());
 60 |     exit(-1);
 61 | }
 62 | ```
 63 |
 64 | An example is included, which is built automatically for the target `all`. It can also be built separately:
 65 |
 66 |   `make bin/example_c`
 67 |
 68 | Building with GPU support
 69 | -------------------------
 70 |
 71 | For GPU support, a separate dynamic library in the "c_api/gpu" directory needs to be built.
 72 |
 73 |   `make`
 74 |
 75 | The "gpufaiss_c" dynamic library contains the GPU and CPU implementations of Faiss, which means that
 76 | it can be used in place of "faiss_c". The same library will dynamically link with the CUDA runtime
 77 | and cuBLAS.
 78 |
 79 | Using the GPU with the C API
 80 | ----------------------------
 81 |
 82 | A standard GPU resources object can be obtained by the name `FaissStandardGpuResources`:
 83 |
 84 | ```c
 85 | FaissStandardGpuResources* gpu_res = NULL;
 86 | int c = faiss_StandardGpuResources_new(&gpu_res);
 87 | if (c) {
 88 |     printf("%s", faiss_get_last_error());
 89 |     exit(-1);
 90 | }
 91 | ```
 92 |
 93 | Similarly to the C++ API, a CPU index can be converted to a GPU index:
 94 |
 95 | ```c
 96 | FaissIndex* cpu_index = NULL;
 97 | int c = faiss_index_factory(&cpu_index, d, "Flat", METRIC_L2);
 98 | if (c) { /* ... */ }
 99 | FaissGpuIndex* gpu_index = NULL;
100 | c = faiss_index_cpu_to_gpu(gpu_res, 0, cpu_index, &gpu_index);
101 | if (c) { /* ... */ }
102 | ```
103 |
104 | A more complete example is available by the name `bin/example_gpu_c`.
105 |


--------------------------------------------------------------------------------
/contrib/README.md:
--------------------------------------------------------------------------------
 1 |
 2 | # The contrib modules
 3 |
 4 | The contrib directory contains helper modules for Faiss for various tasks.
 5 |
 6 | ## Code structure
 7 |
 8 | The contrib directory gets compiled in the module faiss.contrib.
 9 | Note that although some of the modules may depend on additional modules (eg. GPU Faiss, pytorch, hdf5), they are not necessarily compiled in to avoid adding dependencies. It is the user's responsibility to provide them.
10 |
11 | In contrib, we are progressively dropping python2 support.
12 |
13 | ## List of contrib modules
14 |
15 | ### rpc.py
16 |
17 | A very simple Remote Procedure Call library, where function parameters and results are pickled, for use with client_server.py
18 |
19 | ### client_server.py
20 |
21 | The server handles requests to a Faiss index. The client calls the remote index.
22 | This is mainly to shard datasets over several machines, see [Distributed index](https://github.com/facebookresearch/faiss/wiki/Indexes-that-do-not-fit-in-RAM#distributed-index)
23 |
24 | ### ondisk.py
25 |
26 | Encloses the main logic to merge indexes into an on-disk index.
27 | See [On-disk storage](https://github.com/facebookresearch/faiss/wiki/Indexes-that-do-not-fit-in-RAM#on-disk-storage)
28 |
29 | ### exhaustive_search.py
30 |
31 | Computes the ground-truth search results for a dataset that possibly does not fit in RAM. Uses GPU if available.
32 | Tested in `tests/test_contrib.TestComputeGT`
33 |
34 | ### torch_utils.py
35 |
36 | Interoperability functions for pytorch and Faiss: Importing this will allow pytorch Tensors (CPU or GPU) to be used as arguments to Faiss indexes and other functions. Torch GPU tensors can only be used with Faiss GPU indexes. If this is imported with a package that supports Faiss GPU, the necessary stream synchronization with the current pytorch stream will be automatically performed.
37 |
38 | Numpy ndarrays can continue to be used in the Faiss python interface after importing this file. All arguments must be uniformly either numpy ndarrays or Torch tensors; no mixing is allowed.
39 |
40 | Tested in `tests/test_contrib_torch.py` (CPU) and `gpu/test/test_contrib_torch_gpu.py` (GPU).
41 |
42 | ### inspect_tools.py
43 |
44 | Functions to inspect C++ objects wrapped by SWIG. Most often this just means reading
45 | fields and converting them to the proper python array.
46 |
47 | ### ivf_tools.py
48 |
49 | A few functions to override the coarse quantizer in IVF, providing additional flexibility for assignment.
50 |
51 | ### datasets.py
52 |
53 | (may require h5py)
54 |
55 | Definition of how to access data for some standard datasets.
56 |
57 | ### factory_tools.py
58 |
59 | Functions related to factory strings.
60 |
61 | ### evaluation.py
62 |
63 | A few non-trivial evaluation functions for search results
64 |
65 | ### clustering.py
66 |
67 | Contains:
68 |
69 | - a Python implementation of kmeans, that can be used for special datatypes (eg. sparse matrices).
70 |
71 | - a 2-level clustering routine and a function that can apply it to train an IndexIVF
72 |
73 | ### big_batch_search.py
74 |
75 | Search IVF indexes with one centroid after another. Useful for large
76 | databases that do not fit in RAM *and* a large number of queries.
77 |


--------------------------------------------------------------------------------
/contrib/torch/README.md:
--------------------------------------------------------------------------------
1 | # The Torch contrib
2 |
3 | This contrib directory contains a few Pytorch routines that
4 | are useful for similarity search. They do not necessarily depend on Faiss.
5 |
6 | The code is designed to work with CPU and GPU tensors.
7 |


--------------------------------------------------------------------------------
/demos/README.md:
--------------------------------------------------------------------------------
 1 |
 2 |
 3 | Demos for a few Faiss functionalities
 4 | =====================================
 5 |
 6 |
 7 | demo_auto_tune.py
 8 | -----------------
 9 |
10 | Demonstrates the auto-tuning functionality of Faiss
11 |
12 |
13 | demo_ondisk_ivf.py
14 | ------------------
15 |
16 | Shows how to construct a Faiss index that stores the inverted file
17 | data on disk, eg. when it does not fit in RAM. The script works on a
18 | small dataset (sift1M) for demonstration and proceeds in stages:
19 |
20 | 0: train on the dataset
21 |
22 | 1-4: build 4 indexes, each containing 1/4 of the dataset. This can be
23 | done in parallel on several machines
24 |
25 | 5: merge the 4 indexes into one that is written directly to disk
26 | (needs not to fit in RAM)
27 |
28 | 6: load and test the index
29 |


--------------------------------------------------------------------------------
/demos/offline_ivf/README.md:
--------------------------------------------------------------------------------
 1 |
 2 | # Offline IVF
 3 |
 4 | This folder contains the code for the offline ivf algorithm powered by faiss big batch search.
 5 |
 6 | Create a conda env:
 7 |
 8 | `conda create --name oivf python=3.10`
 9 |
10 | `conda activate oivf`
11 |
12 | `conda install -c pytorch/label/nightly -c nvidia faiss-gpu=1.7.4`
13 |
14 | `conda install tqdm`
15 |
16 | `conda install pyyaml`
17 |
18 | `conda install -c conda-forge submitit`
19 |
20 |
21 | ## Run book
22 |
23 | 1. Optionally shard your dataset (see create_sharded_dataset.py) and create the corresponding yaml file `config_ssnpp.yaml`. You can use `generate_config.py` by specifying the root directory of your dataset and the files with the data shards
24 |
25 | `python generate_config`
26 |
27 | 2. Run the train index command
28 |
29 | `python run.py --command train_index --config config_ssnpp.yaml --xb ssnpp_1B`
30 |
31 |
32 | 3. Run the index-shard command so it produces sharded indexes, required for the search step
33 |
34 | `python run.py --command index_shard --config config_ssnpp.yaml --xb ssnpp_1B`
35 |
36 |
37 | 6. Send jobs to the cluster to run search
38 |
39 | `python run.py  --command search --config config_ssnpp.yaml --xb ssnpp_1B  --cluster_run --partition <PARTITION-NAME>`
40 |
41 |
42 | Remarks about the `search` command: it is assumed that the database vectors are the query vectors when performing the search step.
43 | a. If the query vectors are different than the database vectors, it should be passed in the xq argument
44 | b. A new dataset needs to be prepared (step 1) before passing it to the query vectors argument `–xq`
45 |
46 | `python run.py --command search --config config_ssnpp.yaml --xb ssnpp_1B --xq <QUERIES_DATASET_NAME>`
47 |
48 |
49 | 6. We can always run the consistency-check for sanity checks!
50 |
51 | `python run.py  --command consistency_check--config config_ssnpp.yaml --xb ssnpp_1B`
52 |
53 |


--------------------------------------------------------------------------------
/demos/rocksdb_ivf/README.md:
--------------------------------------------------------------------------------
 1 | # Storing Faiss inverted lists in RocksDB
 2 |
 3 | Demo of storing the inverted lists of any IVF index in RocksDB or any similar key-value store which supports the prefix scan operation.
 4 |
 5 | # How to build
 6 |
 7 | We use conda to create the build environment for simplicity. Only tested on Linux x86.
 8 |
 9 | ```
10 | conda create -n rocksdb_ivf
11 | conda activate rocksdb_ivf
12 | conda install pytorch::faiss-cpu conda-forge::rocksdb cmake make gxx_linux-64 sysroot_linux-64
13 | cd ~/faiss/demos/rocksdb_ivf
14 | cmake -B build .
15 | make -C build -j$(nproc)
16 | ```
17 |
18 | # Run the example
19 |
20 | ```
21 | cd ~/faiss/demos/rocksdb_ivf/build
22 | ./rocksdb_ivf test_db
23 | ```
24 |


--------------------------------------------------------------------------------
└── tutorial
    └── python
        ├── 1-Flat.py
        ├── 2-IVFFlat.py
        ├── 3-IVFPQ.py
        ├── 4-GPU.py
        ├── 5-Multiple-GPUs.py
        ├── 7-PQFastScan.py
        ├── 8-PQFastScanRefine.py
        └── 9-RefineComparison.py


/tutorial/python/1-Flat.py:
--------------------------------------------------------------------------------
 1 | # Copyright (c) Meta Platforms, Inc. and affiliates.
 2 | #
 3 | # This source code is licensed under the MIT license found in the
 4 | # LICENSE file in the root directory of this source tree.
 5 |
 6 | import numpy as np
 7 |
 8 | d = 64                           # dimension
 9 | nb = 100000                      # database size
10 | nq = 10000                       # nb of queries
11 | np.random.seed(1234)             # make reproducible
12 | xb = np.random.random((nb, d)).astype('float32')
13 | xb[:, 0] += np.arange(nb) / 1000.
14 | xq = np.random.random((nq, d)).astype('float32')
15 | xq[:, 0] += np.arange(nq) / 1000.
16 |
17 | import faiss                   # make faiss available
18 | index = faiss.IndexFlatL2(d)   # build the index
19 | print(index.is_trained)
20 | index.add(xb)                  # add vectors to the index
21 | print(index.ntotal)
22 |
23 | k = 4                          # we want to see 4 nearest neighbors
24 | D, I = index.search(xb[:5], k) # sanity check
25 | print(I)
26 | print(D)
27 | D, I = index.search(xq, k)     # actual search
28 | print(I[:5])                   # neighbors of the 5 first queries
29 | print(I[-5:])                  # neighbors of the 5 last queries
30 |


--------------------------------------------------------------------------------
/tutorial/python/2-IVFFlat.py:
--------------------------------------------------------------------------------
 1 | # Copyright (c) Meta Platforms, Inc. and affiliates.
 2 | #
 3 | # This source code is licensed under the MIT license found in the
 4 | # LICENSE file in the root directory of this source tree.
 5 |
 6 | import numpy as np
 7 |
 8 | d = 64                           # dimension
 9 | nb = 100000                      # database size
10 | nq = 10000                       # nb of queries
11 | np.random.seed(1234)             # make reproducible
12 | xb = np.random.random((nb, d)).astype('float32')
13 | xb[:, 0] += np.arange(nb) / 1000.
14 | xq = np.random.random((nq, d)).astype('float32')
15 | xq[:, 0] += np.arange(nq) / 1000.
16 |
17 | import faiss
18 |
19 | nlist = 100
20 | k = 4
21 | quantizer = faiss.IndexFlatL2(d)  # the other index
22 | index = faiss.IndexIVFFlat(quantizer, d, nlist, faiss.METRIC_L2)
23 | # here we specify METRIC_L2, by default it performs inner-product search
24 |
25 | assert not index.is_trained
26 | index.train(xb)
27 | assert index.is_trained
28 |
29 | index.add(xb)                  # add may be a bit slower as well
30 | D, I = index.search(xq, k)     # actual search
31 | print(I[-5:])                  # neighbors of the 5 last queries
32 | index.nprobe = 10              # default nprobe is 1, try a few more
33 | D, I = index.search(xq, k)
34 | print(I[-5:])                  # neighbors of the 5 last queries
35 |


--------------------------------------------------------------------------------
/tutorial/python/3-IVFPQ.py:
--------------------------------------------------------------------------------
 1 | # Copyright (c) Meta Platforms, Inc. and affiliates.
 2 | #
 3 | # This source code is licensed under the MIT license found in the
 4 | # LICENSE file in the root directory of this source tree.
 5 |
 6 | import numpy as np
 7 |
 8 | d = 64                           # dimension
 9 | nb = 100000                      # database size
10 | nq = 10000                       # nb of queries
11 | np.random.seed(1234)             # make reproducible
12 | xb = np.random.random((nb, d)).astype('float32')
13 | xb[:, 0] += np.arange(nb) / 1000.
14 | xq = np.random.random((nq, d)).astype('float32')
15 | xq[:, 0] += np.arange(nq) / 1000.
16 |
17 | import faiss
18 |
19 | nlist = 100
20 | m = 8
21 | k = 4
22 | quantizer = faiss.IndexFlatL2(d)  # this remains the same
23 | index = faiss.IndexIVFPQ(quantizer, d, nlist, m, 8)
24 |                                   # 8 specifies that each sub-vector is encoded as 8 bits
25 | index.train(xb)
26 | index.add(xb)
27 | D, I = index.search(xb[:5], k) # sanity check
28 | print(I)
29 | print(D)
30 | index.nprobe = 10              # make comparable with experiment above
31 | D, I = index.search(xq, k)     # search
32 | print(I[-5:])
33 |


--------------------------------------------------------------------------------
/tutorial/python/4-GPU.py:
--------------------------------------------------------------------------------
 1 | # Copyright (c) Meta Platforms, Inc. and affiliates.
 2 | #
 3 | # This source code is licensed under the MIT license found in the
 4 | # LICENSE file in the root directory of this source tree.
 5 |
 6 | import numpy as np
 7 |
 8 | d = 64                           # dimension
 9 | nb = 100000                      # database size
10 | nq = 10000                       # nb of queries
11 | np.random.seed(1234)             # make reproducible
12 | xb = np.random.random((nb, d)).astype('float32')
13 | xb[:, 0] += np.arange(nb) / 1000.
14 | xq = np.random.random((nq, d)).astype('float32')
15 | xq[:, 0] += np.arange(nq) / 1000.
16 |
17 | import faiss                     # make faiss available
18 |
19 | res = faiss.StandardGpuResources()  # use a single GPU
20 |
21 | ## Using a flat index
22 |
23 | index_flat = faiss.IndexFlatL2(d)  # build a flat (CPU) index
24 |
25 | # make it a flat GPU index
26 | gpu_index_flat = faiss.index_cpu_to_gpu(res, 0, index_flat)
27 |
28 | gpu_index_flat.add(xb)         # add vectors to the index
29 | print(gpu_index_flat.ntotal)
30 |
31 | k = 4                          # we want to see 4 nearest neighbors
32 | D, I = gpu_index_flat.search(xq, k)  # actual search
33 | print(I[:5])                   # neighbors of the 5 first queries
34 | print(I[-5:])                  # neighbors of the 5 last queries
35 |
36 |
37 | ## Using an IVF index
38 |
39 | nlist = 100
40 | quantizer = faiss.IndexFlatL2(d)  # the other index
41 | index_ivf = faiss.IndexIVFFlat(quantizer, d, nlist, faiss.METRIC_L2)
42 | # here we specify METRIC_L2, by default it performs inner-product search
43 |
44 | # make it an IVF GPU index
45 | gpu_index_ivf = faiss.index_cpu_to_gpu(res, 0, index_ivf)
46 |
47 | assert not gpu_index_ivf.is_trained
48 | gpu_index_ivf.train(xb)        # add vectors to the index
49 | assert gpu_index_ivf.is_trained
50 |
51 | gpu_index_ivf.add(xb)          # add vectors to the index
52 | print(gpu_index_ivf.ntotal)
53 |
54 | k = 4                          # we want to see 4 nearest neighbors
55 | D, I = gpu_index_ivf.search(xq, k)  # actual search
56 | print(I[:5])                   # neighbors of the 5 first queries
57 | print(I[-5:])                  # neighbors of the 5 last queries
58 |


--------------------------------------------------------------------------------
/tutorial/python/5-Multiple-GPUs.py:
--------------------------------------------------------------------------------
 1 | # Copyright (c) Meta Platforms, Inc. and affiliates.
 2 | #
 3 | # This source code is licensed under the MIT license found in the
 4 | # LICENSE file in the root directory of this source tree.
 5 |
 6 | import numpy as np
 7 |
 8 | d = 64                           # dimension
 9 | nb = 100000                      # database size
10 | nq = 10000                       # nb of queries
11 | np.random.seed(1234)             # make reproducible
12 | xb = np.random.random((nb, d)).astype('float32')
13 | xb[:, 0] += np.arange(nb) / 1000.
14 | xq = np.random.random((nq, d)).astype('float32')
15 | xq[:, 0] += np.arange(nq) / 1000.
16 |
17 | import faiss                     # make faiss available
18 |
19 | ngpus = faiss.get_num_gpus()
20 |
21 | print("number of GPUs:", ngpus)
22 |
23 | cpu_index = faiss.IndexFlatL2(d)
24 |
25 | gpu_index = faiss.index_cpu_to_all_gpus(  # build the index
26 |     cpu_index
27 | )
28 |
29 | gpu_index.add(xb)              # add vectors to the index
30 | print(gpu_index.ntotal)
31 |
32 | k = 4                          # we want to see 4 nearest neighbors
33 | D, I = gpu_index.search(xq, k) # actual search
34 | print(I[:5])                   # neighbors of the 5 first queries
35 | print(I[-5:])                  # neighbors of the 5 last queries
36 |


--------------------------------------------------------------------------------
/tutorial/python/7-PQFastScan.py:
--------------------------------------------------------------------------------
 1 | # Copyright (c) Meta Platforms, Inc. and affiliates.
 2 | #
 3 | # This source code is licensed under the MIT license found in the
 4 | # LICENSE file in the root directory of this source tree.
 5 |
 6 | import faiss
 7 | import numpy as np
 8 |
 9 | d = 64                           # dimension
10 | nb = 100000                      # database size
11 | nq = 10000                       # nb of queries
12 | np.random.seed(1234)             # make reproducible
13 | xb = np.random.random((nb, d)).astype('float32')    # 64-dim *nb queries
14 | xb[:, 0] += np.arange(nb) / 1000.
15 | xq = np.random.random((nq, d)).astype('float32')
16 | xq[:, 0] += np.arange(nq) / 1000.
17 |
18 | m = 8   # 8 specifies that the number of sub-vector is 8
19 | k = 4   # number of dimension in etracted vector
20 | n_bit = 4   # 4 specifies that each sub-vector is encoded as 4 bits
21 | bbs = 32    # build block size ( bbs % 32 == 0 ) for PQ
22 | index = faiss.IndexPQFastScan(d, m, n_bit, faiss.METRIC_L2, bbs)
23 | # construct FastScan Index
24 |
25 | assert not index.is_trained
26 | index.train(xb)     # Train vectors data index within mockup database
27 | assert index.is_trained
28 |
29 | index.add(xb)
30 | D, I = index.search(xb[:5], k)  # sanity check
31 | print(I)
32 | print(D)
33 | index.nprobe = 10              # make comparable with experiment above
34 | D, I = index.search(xq, k)     # search
35 | print(I[-5:])               # neighbors of the 5 last queries
36 |


--------------------------------------------------------------------------------
/tutorial/python/8-PQFastScanRefine.py:
--------------------------------------------------------------------------------
 1 | # Copyright (c) Meta Platforms, Inc. and affiliates.
 2 | #
 3 | # This source code is licensed under the MIT license found in the
 4 | # LICENSE file in the root directory of this source tree.
 5 |
 6 | import faiss
 7 | import numpy as np
 8 |
 9 | d = 64                           # dimension
10 | nb = 100000                      # database size
11 | nq = 10000                       # nb of queries
12 | np.random.seed(1234)             # make reproducible
13 | xb = np.random.random((nb, d)).astype('float32')    # 64-dim *nb queries
14 | xb[:, 0] += np.arange(nb) / 1000.
15 | xq = np.random.random((nq, d)).astype('float32')
16 | xq[:, 0] += np.arange(nq) / 1000.
17 |
18 | m = 8  # 8 specifies that the number of sub-vector is 8
19 | k = 4  # number of dimension in etracted vector
20 | n_bit = 4  # 4 specifies that each sub-vector is encoded as 4 bits
21 | bbs = 32  # build block size ( bbs % 32 == 0 ) for PQ
22 |
23 | index = faiss.IndexPQFastScan(d, m, n_bit, faiss.METRIC_L2)
24 | index_refine = faiss.IndexRefineFlat(index)
25 | # construct FastScan and run index refinement
26 |
27 | assert not index_refine.is_trained
28 | index_refine.train(xb)  # Train vectors data index within mockup database
29 | assert index_refine.is_trained
30 |
31 | index_refine.add(xb)
32 | params = faiss.IndexRefineSearchParameters(k_factor=3)
33 | D, I = index_refine.search(xq[:5], 10, params=params)
34 | print(I)
35 | print(D)
36 | index.nprobe = 10  # make comparable with experiment above
37 | D, I = index.search(xq[:5], k)  # search
38 | print(I[-5:])
39 |


--------------------------------------------------------------------------------
/tutorial/python/9-RefineComparison.py:
--------------------------------------------------------------------------------
 1 | # Copyright (c) Meta Platforms, Inc. and affiliates.
 2 | #
 3 | # This source code is licensed under the MIT license found in the
 4 | # LICENSE file in the root directory of this source tree.
 5 |
 6 | import faiss
 7 |
 8 | from faiss.contrib.evaluation import knn_intersection_measure
 9 | from faiss.contrib import datasets
10 |
11 | # 64-dim vectors, 50000 vectors in the training, 100000 in database,
12 | # 10000 in queries, dtype ('float32')
13 | ds = datasets.SyntheticDataset(64, 50000, 100000, 10000)
14 | d = 64                           # dimension
15 |
16 | # Constructing the refine PQ index with SQfp16 with index factory
17 | index_fp16 = faiss.index_factory(d, 'PQ32x4fs,Refine(SQfp16)')
18 | index_fp16.train(ds.get_train())
19 | index_fp16.add(ds.get_database())
20 |
21 | # Constructing the refine PQ index with SQ8
22 | index_sq8 = faiss.index_factory(d, 'PQ32x4fs,Refine(SQ8)')
23 | index_sq8.train(ds.get_train())
24 | index_sq8.add(ds.get_database())
25 |
26 | # Parameterization on k factor while doing search for index refinement
27 | k_factor = 3.0
28 | params = faiss.IndexRefineSearchParameters(k_factor=k_factor)
29 |
30 | # Perform index search using different index refinement
31 | D_fp16, I_fp16 = index_fp16.search(ds.get_queries(), 100, params=params)
32 | D_sq8, I_sq8 = index_sq8.search(ds.get_queries(), 100, params=params)
33 |
34 | # Calculating knn intersection measure for different index types on refinement
35 | KIM_fp16 = knn_intersection_measure(I_fp16, ds.get_groundtruth())
36 | KIM_sq8 = knn_intersection_measure(I_sq8, ds.get_groundtruth())
37 |
38 | # KNN intersection measure accuracy shows that choosing SQ8 impacts accuracy
39 | assert (KIM_fp16 > KIM_sq8)
40 |
41 | print(I_sq8[:5])
42 | print(I_fp16[:5])
43 |


--------------------------------------------------------------------------------
└── demos
    ├── demo_auto_tune.py
    ├── demo_client_server_ivf.py
    ├── demo_distributed_kmeans_torch.py
    ├── demo_ondisk_ivf.py
    ├── demo_qinco.py
    ├── index_pq_flat_separate_codes_from_codebook.py
    └── offline_ivf
        ├── __init__.py
        ├── create_sharded_ssnpp_files.py
        ├── dataset.py
        ├── generate_config.py
        ├── offline_ivf.py
        ├── run.py
        ├── tests
            ├── test_iterate_input.py
            ├── test_offline_ivf.py
            └── testing_utils.py
        └── utils.py


/demos/demo_auto_tune.py:
--------------------------------------------------------------------------------
  1 | #!/usr/bin/env python2
  2 | # Copyright (c) Meta Platforms, Inc. and affiliates.
  3 | #
  4 | # This source code is licensed under the MIT license found in the
  5 | # LICENSE file in the root directory of this source tree.
  6 |
  7 | from __future__ import print_function
  8 | import os
  9 | import time
 10 | import numpy as np
 11 |
 12 | try:
 13 |     import matplotlib
 14 |     matplotlib.use('Agg')
 15 |     from matplotlib import pyplot
 16 |     graphical_output = True
 17 | except ImportError:
 18 |     graphical_output = False
 19 |
 20 | import faiss
 21 |
 22 | #################################################################
 23 | # Small I/O functions
 24 | #################################################################
 25 |
 26 | def ivecs_read(fname):
 27 |     a = np.fromfile(fname, dtype="int32")
 28 |     d = a[0]
 29 |     return a.reshape(-1, d + 1)[:, 1:].copy()
 30 |
 31 | def fvecs_read(fname):
 32 |     return ivecs_read(fname).view('float32')
 33 |
 34 |
 35 | def plot_OperatingPoints(ops, nq, **kwargs):
 36 |     ops = ops.optimal_pts
 37 |     n = ops.size() * 2 - 1
 38 |     pyplot.plot([ops.at( i      // 2).perf for i in range(n)],
 39 |                 [ops.at((i + 1) // 2).t / nq * 1000 for i in range(n)],
 40 |                 **kwargs)
 41 |
 42 |
 43 | #################################################################
 44 | # prepare common data for all indexes
 45 | #################################################################
 46 |
 47 |
 48 |
 49 | t0 = time.time()
 50 |
 51 | print("load data")
 52 |
 53 | xt = fvecs_read("sift1M/sift_learn.fvecs")
 54 | xb = fvecs_read("sift1M/sift_base.fvecs")
 55 | xq = fvecs_read("sift1M/sift_query.fvecs")
 56 |
 57 | d = xt.shape[1]
 58 |
 59 | print("load GT")
 60 |
 61 | gt = ivecs_read("sift1M/sift_groundtruth.ivecs")
 62 | gt = gt.astype('int64')
 63 | k = gt.shape[1]
 64 |
 65 | print("prepare criterion")
 66 |
 67 | # criterion = 1-recall at 1
 68 | crit = faiss.OneRecallAtRCriterion(xq.shape[0], 1)
 69 | crit.set_groundtruth(None, gt)
 70 | crit.nnn = k
 71 |
 72 | # indexes that are useful when there is no limitation on memory usage
 73 | unlimited_mem_keys = [
 74 |     "IMI2x10,Flat", "IMI2x11,Flat",
 75 |     "IVF4096,Flat", "IVF16384,Flat",
 76 |     "PCA64,IMI2x10,Flat"]
 77 |
 78 | # memory limited to 16 bytes / vector
 79 | keys_mem_16 = [
 80 |     'IMI2x10,PQ16', 'IVF4096,PQ16',
 81 |     'IMI2x10,PQ8+8', 'OPQ16_64,IMI2x10,PQ16'
 82 |     ]
 83 |
 84 | # limited to 32 bytes / vector
 85 | keys_mem_32 = [
 86 |     'IMI2x10,PQ32', 'IVF4096,PQ32', 'IVF16384,PQ32',
 87 |     'IMI2x10,PQ16+16',
 88 |     'OPQ32,IVF4096,PQ32', 'IVF4096,PQ16+16', 'OPQ16,IMI2x10,PQ16+16'
 89 |     ]
 90 |
 91 | # indexes that can run on the GPU
 92 | keys_gpu = [
 93 |     "PCA64,IVF4096,Flat",
 94 |     "PCA64,Flat", "Flat", "IVF4096,Flat", "IVF16384,Flat",
 95 |     "IVF4096,PQ32"]
 96 |
 97 |
 98 | keys_to_test = unlimited_mem_keys
 99 | use_gpu = False
100 |
101 |
102 | if use_gpu:
103 |     # if this fails, it means that the GPU version was not comp
104 |     assert faiss.StandardGpuResources, \
105 |         "Faiss was not compiled with GPU support, or loading _swigfaiss_gpu.so failed"
106 |     res = faiss.StandardGpuResources()
107 |     dev_no = 0
108 |
109 | # remember results from other index types
110 | op_per_key = []
111 |
112 |
113 | # keep track of optimal operating points seen so far
114 | op = faiss.OperatingPoints()
115 |
116 |
117 | for index_key in keys_to_test:
118 |
119 |     print("============ key", index_key)
120 |
121 |     # make the index described by the key
122 |     index = faiss.index_factory(d, index_key)
123 |
124 |
125 |     if use_gpu:
126 |         # transfer to GPU (may be partial)
127 |         index = faiss.index_cpu_to_gpu(res, dev_no, index)
128 |         params = faiss.GpuParameterSpace()
129 |     else:
130 |         params = faiss.ParameterSpace()
131 |
132 |     params.initialize(index)
133 |
134 |     print("[%.3f s] train & add" % (time.time() - t0))
135 |
136 |     index.train(xt)
137 |     index.add(xb)
138 |
139 |     print("[%.3f s] explore op points" % (time.time() - t0))
140 |
141 |     # find operating points for this index
142 |     opi = params.explore(index, xq, crit)
143 |
144 |     print("[%.3f s] result operating points:" % (time.time() - t0))
145 |     opi.display()
146 |
147 |     # update best operating points so far
148 |     op.merge_with(opi, index_key + " ")
149 |
150 |     op_per_key.append((index_key, opi))
151 |
152 |     if graphical_output:
153 |         # graphical output (to tmp/ subdirectory)
154 |
155 |         fig = pyplot.figure(figsize=(12, 9))
156 |         pyplot.xlabel("1-recall at 1")
157 |         pyplot.ylabel("search time (ms/query, %d threads)" % faiss.omp_get_max_threads())
158 |         pyplot.gca().set_yscale('log')
159 |         pyplot.grid()
160 |         for i2, opi2 in op_per_key:
161 |             plot_OperatingPoints(opi2, crit.nq, label = i2, marker = 'o')
162 |         # plot_OperatingPoints(op, crit.nq, label = 'best', marker = 'o', color = 'r')
163 |         pyplot.legend(loc=2)
164 |         fig.savefig('tmp/demo_auto_tune.png')
165 |
166 |
167 | print("[%.3f s] final result:" % (time.time() - t0))
168 |
169 | op.display()
170 |


--------------------------------------------------------------------------------
/demos/demo_client_server_ivf.py:
--------------------------------------------------------------------------------
 1 | #!/usr/bin/env python3
 2 | # Copyright (c) Meta Platforms, Inc. and affiliates.
 3 | #
 4 | # This source code is licensed under the MIT license found in the
 5 | # LICENSE file in the root directory of this source tree.
 6 |
 7 | import sys
 8 | import numpy as np
 9 | import faiss
10 |
11 | from faiss.contrib.client_server import run_index_server, ClientIndex
12 |
13 |
14 | #################################################################
15 | # Small I/O functions
16 | #################################################################
17 |
18 |
19 | def ivecs_read(fname):
20 |     a = np.fromfile(fname, dtype='int32')
21 |     d = a[0]
22 |     return a.reshape(-1, d + 1)[:, 1:].copy()
23 |
24 |
25 | def fvecs_read(fname):
26 |     return ivecs_read(fname).view('float32')
27 |
28 |
29 | #################################################################
30 | #  Main program
31 | #################################################################
32 |
33 | stage = int(sys.argv[1])
34 |
35 | tmpdir = '/tmp/'
36 |
37 | if stage == 0:
38 |     # train the index
39 |     xt = fvecs_read("sift1M/sift_learn.fvecs")
40 |     index = faiss.index_factory(xt.shape[1], "IVF4096,Flat")
41 |     print("training index")
42 |     index.train(xt)
43 |     print("write " + tmpdir + "trained.index")
44 |     faiss.write_index(index, tmpdir + "trained.index")
45 |
46 |
47 | if 1 <= stage <= 4:
48 |     # add 1/4 of the database to 4 independent indexes
49 |     bno = stage - 1
50 |     xb = fvecs_read("sift1M/sift_base.fvecs")
51 |     i0, i1 = int(bno * xb.shape[0] / 4), int((bno + 1) * xb.shape[0] / 4)
52 |     index = faiss.read_index(tmpdir + "trained.index")
53 |     print("adding vectors %d:%d" % (i0, i1))
54 |     index.add_with_ids(xb[i0:i1], np.arange(i0, i1))
55 |     print("write " + tmpdir + "block_%d.index" % bno)
56 |     faiss.write_index(index, tmpdir + "block_%d.index" % bno)
57 |
58 |
59 | machine_ports = [
60 |     ('localhost', 12010),
61 |     ('localhost', 12011),
62 |     ('localhost', 12012),
63 |     ('localhost', 12013),
64 | ]
65 | v6 = False
66 |
67 | if 5 <= stage <= 8:
68 |     # load an index slice and launch index
69 |     bno = stage - 5
70 |
71 |     fname = tmpdir + "block_%d.index" % bno
72 |     print("read " + fname)
73 |     index = faiss.read_index(fname)
74 |
75 |     port = machine_ports[bno][1]
76 |     run_index_server(index, port, v6=v6)
77 |
78 |
79 | if stage == 9:
80 |     client_index = ClientIndex(machine_ports)
81 |     print('index size:', client_index.ntotal)
82 |     client_index.set_nprobe(16)
83 |
84 |     # load query vectors and ground-truth
85 |     xq = fvecs_read("sift1M/sift_query.fvecs")
86 |     gt = ivecs_read("sift1M/sift_groundtruth.ivecs")
87 |
88 |     D, I = client_index.search(xq, 5)
89 |
90 |     recall_at_1 = (I[:, :1] == gt[:, :1]).sum() / float(xq.shape[0])
91 |     print("recall@1: %.3f" % recall_at_1)
92 |


--------------------------------------------------------------------------------
/demos/demo_distributed_kmeans_torch.py:
--------------------------------------------------------------------------------
  1 | # Copyright (c) Meta Platforms, Inc. and affiliates.
  2 | #
  3 | # This source code is licensed under the MIT license found in the
  4 | # LICENSE file in the root directory of this source tree.
  5 |
  6 | import numpy as np
  7 |
  8 | import torch
  9 | import torch.distributed
 10 |
 11 | import faiss
 12 |
 13 | import faiss.contrib.torch_utils
 14 | from faiss.contrib.torch import clustering
 15 | from faiss.contrib import datasets
 16 |
 17 |
 18 | class DatasetAssignDistributedGPU(clustering.DatasetAssign):
 19 |     """
 20 |     There is one instance per worker, each worker has a dataset shard.
 21 |     The non-master workers do not run through the k-means function, so some
 22 |     code has run it to keep the workers in sync.
 23 |     """
 24 |
 25 |     def __init__(self, res, x, rank, nproc):
 26 |         clustering.DatasetAssign.__init__(self, x)
 27 |         self.res = res
 28 |         self.rank = rank
 29 |         self.nproc = nproc
 30 |         self.device = x.device
 31 |
 32 |         n = len(x)
 33 |         sizes = torch.zeros(nproc, device=self.device, dtype=torch.int64)
 34 |         sizes[rank] = n
 35 |         torch.distributed.all_gather(
 36 |             [sizes[i:i + 1] for i in range(nproc)], sizes[rank:rank + 1])
 37 |         self.sizes = sizes.cpu().numpy()
 38 |
 39 |         # begin & end of each shard
 40 |         self.cs = np.zeros(nproc + 1, dtype='int64')
 41 |         self.cs[1:] = np.cumsum(self.sizes)
 42 |
 43 |     def count(self):
 44 |         return int(self.sizes.sum())
 45 |
 46 |     def int_to_slaves(self, i):
 47 |         " broadcast an int to all workers "
 48 |         rank = self.rank
 49 |         tab = torch.zeros(1, device=self.device, dtype=torch.int64)
 50 |         if rank == 0:
 51 |             tab[0] = i
 52 |         else:
 53 |             assert i is None
 54 |         torch.distributed.broadcast(tab, 0)
 55 |         return tab.item()
 56 |
 57 |     def get_subset(self, indices):
 58 |         rank = self.rank
 59 |         assert rank == 0 or indices is None
 60 |
 61 |         len_indices = self.int_to_slaves(len(indices) if rank == 0 else None)
 62 |
 63 |         if rank == 0:
 64 |             indices = torch.from_numpy(indices).to(self.device)
 65 |         else:
 66 |             indices = torch.zeros(
 67 |                 len_indices, dtype=torch.int64, device=self.device)
 68 |         torch.distributed.broadcast(indices, 0)
 69 |
 70 |         # select subset of indices
 71 |
 72 |         i0, i1 = self.cs[rank], self.cs[rank + 1]
 73 |
 74 |         mask = torch.logical_and(indices < i1, indices >= i0)
 75 |         output = torch.zeros(
 76 |             len_indices, self.x.shape[1],
 77 |             dtype=self.x.dtype, device=self.device)
 78 |         output[mask] = self.x[indices[mask] - i0]
 79 |         torch.distributed.reduce(output, 0)  # sum
 80 |         if rank == 0:
 81 |             return output
 82 |         else:
 83 |             return None
 84 |
 85 |     def perform_search(self, centroids):
 86 |         assert False, "shoudl not be called"
 87 |
 88 |     def assign_to(self, centroids, weights=None):
 89 |         assert weights is None
 90 |
 91 |         rank, nproc = self.rank, self.nproc
 92 |         assert rank == 0 or centroids is None
 93 |         nc = self.int_to_slaves(len(centroids) if rank == 0 else None)
 94 |
 95 |         if rank != 0:
 96 |             centroids = torch.zeros(
 97 |                 nc, self.x.shape[1], dtype=self.x.dtype, device=self.device)
 98 |         torch.distributed.broadcast(centroids, 0)
 99 |
100 |         # perform search
101 |         D, I = faiss.knn_gpu(
102 |             self.res, self.x, centroids, 1, device=self.device.index)
103 |
104 |         I = I.ravel()
105 |         D = D.ravel()
106 |
107 |         sum_per_centroid = torch.zeros_like(centroids)
108 |         if weights is None:
109 |             sum_per_centroid.index_add_(0, I, self.x)
110 |         else:
111 |             sum_per_centroid.index_add_(0, I, self.x * weights[:, None])
112 |
113 |         torch.distributed.reduce(sum_per_centroid, 0)
114 |
115 |         if rank == 0:
116 |             # gather deos not support tensors of different sizes
117 |             # should be implemented with point-to-point communication
118 |             assert np.all(self.sizes == self.sizes[0])
119 |             device = self.device
120 |             all_I = torch.zeros(self.count(), dtype=I.dtype, device=device)
121 |             all_D = torch.zeros(self.count(), dtype=D.dtype, device=device)
122 |             torch.distributed.gather(
123 |                 I, [all_I[self.cs[r]:self.cs[r + 1]] for r in range(nproc)],
124 |                 dst=0,
125 |             )
126 |             torch.distributed.gather(
127 |                 D, [all_D[self.cs[r]:self.cs[r + 1]] for r in range(nproc)],
128 |                 dst=0,
129 |             )
130 |             return all_I.cpu().numpy(), all_D, sum_per_centroid
131 |         else:
132 |             torch.distributed.gather(I, None, dst=0)
133 |             torch.distributed.gather(D, None, dst=0)
134 |             return None
135 |
136 |
137 | if __name__ == "__main__":
138 |
139 |     torch.distributed.init_process_group(
140 |         backend="nccl",
141 |     )
142 |     rank = torch.distributed.get_rank()
143 |     nproc = torch.distributed.get_world_size()
144 |
145 |     # current version does only support shards of the same size
146 |     ds = datasets.SyntheticDataset(32, 10000, 0, 0, seed=1234 + rank)
147 |     x = ds.get_train()
148 |
149 |     device = torch.device(f"cuda:{rank}")
150 |
151 |     torch.cuda.set_device(device)
152 |     x = torch.from_numpy(x).to(device)
153 |     res = faiss.StandardGpuResources()
154 |
155 |     da = DatasetAssignDistributedGPU(res, x, rank, nproc)
156 |
157 |     k = 1000
158 |     niter = 25
159 |
160 |     if rank == 0:
161 |         print(f"sizes = {da.sizes}")
162 |         centroids, iteration_stats = clustering.kmeans(
163 |             k, da, niter=niter, return_stats=True)
164 |         print("clusters:", centroids.cpu().numpy())
165 |     else:
166 |         # make sure the iterations are aligned with master
167 |         da.get_subset(None)
168 |
169 |         for _ in range(niter):
170 |             da.assign_to(None)
171 |
172 |     torch.distributed.barrier()
173 |     print("Done")
174 |


--------------------------------------------------------------------------------
/demos/demo_ondisk_ivf.py:
--------------------------------------------------------------------------------
 1 | #!/usr/bin/env python3
 2 | # Copyright (c) Meta Platforms, Inc. and affiliates.
 3 | #
 4 | # This source code is licensed under the MIT license found in the
 5 | # LICENSE file in the root directory of this source tree.
 6 |
 7 | import sys
 8 | import numpy as np
 9 | import faiss
10 | from faiss.contrib.ondisk import merge_ondisk
11 |
12 | #################################################################
13 | # Small I/O functions
14 | #################################################################
15 |
16 |
17 | def ivecs_read(fname):
18 |     a = np.fromfile(fname, dtype='int32')
19 |     d = a[0]
20 |     return a.reshape(-1, d + 1)[:, 1:].copy()
21 |
22 |
23 | def fvecs_read(fname):
24 |     return ivecs_read(fname).view('float32')
25 |
26 |
27 | #################################################################
28 | # Main program
29 | #################################################################
30 |
31 | stage = int(sys.argv[1])
32 |
33 | tmpdir = '/tmp/'
34 |
35 | if stage == 0:
36 |     # train the index
37 |     xt = fvecs_read("sift1M/sift_learn.fvecs")
38 |     index = faiss.index_factory(xt.shape[1], "IVF4096,Flat")
39 |     print("training index")
40 |     index.train(xt)
41 |     print("write " + tmpdir + "trained.index")
42 |     faiss.write_index(index, tmpdir + "trained.index")
43 |
44 |
45 | if 1 <= stage <= 4:
46 |     # add 1/4 of the database to 4 independent indexes
47 |     bno = stage - 1
48 |     xb = fvecs_read("sift1M/sift_base.fvecs")
49 |     i0, i1 = int(bno * xb.shape[0] / 4), int((bno + 1) * xb.shape[0] / 4)
50 |     index = faiss.read_index(tmpdir + "trained.index")
51 |     print("adding vectors %d:%d" % (i0, i1))
52 |     index.add_with_ids(xb[i0:i1], np.arange(i0, i1))
53 |     print("write " + tmpdir + "block_%d.index" % bno)
54 |     faiss.write_index(index, tmpdir + "block_%d.index" % bno)
55 |
56 | if stage == 5:
57 |
58 |     print('loading trained index')
59 |     # construct the output index
60 |     index = faiss.read_index(tmpdir + "trained.index")
61 |
62 |     block_fnames = [
63 |         tmpdir + "block_%d.index" % bno
64 |         for bno in range(4)
65 |     ]
66 |
67 |     merge_ondisk(index, block_fnames, tmpdir + "merged_index.ivfdata")
68 |
69 |     print("write " + tmpdir + "populated.index")
70 |     faiss.write_index(index, tmpdir + "populated.index")
71 |
72 |
73 | if stage == 6:
74 |     # perform a search from disk
75 |     print("read " + tmpdir + "populated.index")
76 |     index = faiss.read_index(tmpdir + "populated.index")
77 |     index.nprobe = 16
78 |
79 |     # load query vectors and ground-truth
80 |     xq = fvecs_read("sift1M/sift_query.fvecs")
81 |     gt = ivecs_read("sift1M/sift_groundtruth.ivecs")
82 |
83 |     D, I = index.search(xq, 5)
84 |
85 |     recall_at_1 = (I[:, :1] == gt[:, :1]).sum() / float(xq.shape[0])
86 |     print("recall@1: %.3f" % recall_at_1)
87 |


--------------------------------------------------------------------------------
/demos/demo_qinco.py:
--------------------------------------------------------------------------------
 1 | # Copyright (c) Meta Platforms, Inc. and affiliates.
 2 | #
 3 | # This source code is licensed under the MIT license found in the
 4 | # LICENSE file in the root directory of this source tree.
 5 |
 6 | """
 7 | This demonstrates how to reproduce the QINCo paper results using the Faiss
 8 | QINCo implementation. The code loads the reference model because training
 9 | is not implemented in Faiss.
10 |
11 | Prepare the data with
12 |
13 | cd /tmp
14 |
15 | # get the reference qinco code
16 | git clone https://github.com/facebookresearch/Qinco.git
17 |
18 | # get the data
19 | wget https://dl.fbaipublicfiles.com/QINCo/datasets/bigann/bigann1M.bvecs
20 |
21 | # get the model
22 | wget https://dl.fbaipublicfiles.com/QINCo/models/bigann_8x8_L2.pt
23 |
24 | """
25 |
26 | import numpy as np
27 | from faiss.contrib.vecs_io import bvecs_mmap
28 | import sys
29 | import time
30 | import torch
31 | import faiss
32 |
33 | # make sure pickle deserialization will work
34 | sys.path.append("/tmp/Qinco")
35 | import model_qinco
36 |
37 | with torch.no_grad():
38 |
39 |     qinco = torch.load("/tmp/bigann_8x8_L2.pt", weights_only=False)
40 |     qinco.eval()
41 |     # print(qinco)
42 |     if True:
43 |         torch.set_num_threads(1)
44 |         faiss.omp_set_num_threads(1)
45 |
46 |     x_base = bvecs_mmap("/tmp/bigann1M.bvecs")[:1000].astype('float32')
47 |     x_scaled = torch.from_numpy(x_base) / qinco.db_scale
48 |
49 |     t0 = time.time()
50 |     codes, _ = qinco.encode(x_scaled)
51 |     x_decoded_scaled = qinco.decode(codes)
52 |     print(f"Pytorch encode {time.time() - t0:.3f} s")
53 |     # multi-thread: 1.13s, single-thread: 7.744
54 |
55 |     x_decoded = x_decoded_scaled.numpy() * qinco.db_scale
56 |
57 |     err = ((x_decoded - x_base) ** 2).sum(1).mean()
58 |     print("MSE=", err)  # = 14211.956, near the L=2 result in Fig 4 of the paper
59 |
60 |     qinco2 = faiss.QINCo(qinco)
61 |     t0 = time.time()
62 |     codes2 = qinco2.encode(faiss.Tensor2D(x_scaled))
63 |     x_decoded2 = qinco2.decode(codes2).numpy() * qinco.db_scale
64 |     print(f"Faiss encode {time.time() - t0:.3f} s")
65 |     # multi-thread: 3.2s, single thread: 7.019
66 |
67 |     # these tests don't work because there are outlier encodings
68 |     # np.testing.assert_array_equal(codes.numpy(), codes2.numpy())
69 |     # np.testing.assert_allclose(x_decoded, x_decoded2)
70 |
71 |     ndiff = (codes.numpy() != codes2.numpy()).sum() / codes.numel()
72 |     assert ndiff < 0.01
73 |     ndiff = (((x_decoded - x_decoded2) ** 2).sum(1) > 1e-5).sum()
74 |     assert ndiff / len(x_base) < 0.01
75 |
76 |     err = ((x_decoded2 - x_base) ** 2).sum(1).mean()
77 |     print("MSE=", err)  # = 14213.551
78 |


--------------------------------------------------------------------------------
/demos/index_pq_flat_separate_codes_from_codebook.py:
--------------------------------------------------------------------------------
  1 | #!/usr/bin/env -S grimaldi --kernel bento_kernel_faiss
  2 | # Copyright (c) Meta Platforms, Inc. and affiliates.
  3 | #
  4 | # This source code is licensed under the MIT license found in the
  5 | # LICENSE file in the root directory of this source tree.
  6 | # fmt: off
  7 | # flake8: noqa
  8 |
  9 |
 10 | """:md
 11 | # Serializing codes separately, with IndexLSH and IndexPQ
 12 |
 13 | Let's say, for example, you have a few vector embeddings per user
 14 | and want to shard a flat index by user so you can re-use the same LSH or PQ method
 15 |  for all users but store each user's codes independently.
 16 |
 17 |
 18 | """
 19 |
 20 | """:py"""
 21 | import faiss
 22 | import numpy as np
 23 |
 24 | """:py"""
 25 | d = 768
 26 | n = 1_000
 27 | ids = np.arange(n).astype('int64')
 28 | training_data = np.random.rand(n, d).astype('float32')
 29 |
 30 | """:py"""
 31 | def read_ids_codes():
 32 |     try:
 33 |         return np.load("/tmp/ids.npy"), np.load("/tmp/codes.npy")
 34 |     except FileNotFoundError:
 35 |         return None, None
 36 |
 37 |
 38 | def write_ids_codes(ids, codes):
 39 |     np.save("/tmp/ids.npy", ids)
 40 |     np.save("/tmp/codes.npy", codes.reshape(len(ids), -1))
 41 |
 42 |
 43 | def write_template_index(template_index):
 44 |     faiss.write_index(template_index, "/tmp/template.index")
 45 |
 46 |
 47 | def read_template_index_instance():
 48 |     return faiss.read_index("/tmp/template.index")
 49 |
 50 | """:md
 51 | ## IndexLSH: separate codes
 52 |
 53 | The first half of this notebook demonstrates how to store LSH codes. Unlike PQ, LSH does not require training. In fact, it's compression method, a random projections matrix, is deterministic on construction based on a random seed value that's [hardcoded](https://github.com/facebookresearch/faiss/blob/2c961cc308ade8a85b3aa10a550728ce3387f625/faiss/IndexLSH.cpp#L35).
 54 | """
 55 |
 56 | """:py"""
 57 | nbits = 1536
 58 |
 59 | """:py"""
 60 | # demonstrating encoding is deterministic
 61 |
 62 | codes = []
 63 | database_vector_float32 = np.random.rand(1, d).astype(np.float32)
 64 | for i in range(10):
 65 |     index = faiss.IndexIDMap2(faiss.IndexLSH(d, nbits))
 66 |     code = index.index.sa_encode(database_vector_float32)
 67 |     codes.append(code)
 68 |
 69 | for i in range(1, 10):
 70 |     assert np.array_equal(codes[0], codes[i])
 71 |
 72 | """:py"""
 73 | # new database vector
 74 |
 75 | ids, codes = read_ids_codes()
 76 | database_vector_id, database_vector_float32 = max(ids) + 1 if ids is not None else 1, np.random.rand(1, d).astype(np.float32)
 77 | index = faiss.IndexIDMap2(faiss.IndexLSH(d, nbits))
 78 |
 79 | code = index.index.sa_encode(database_vector_float32)
 80 |
 81 | if ids is not None and codes is not None:
 82 |     ids = np.concatenate((ids, [database_vector_id]))
 83 |     codes = np.vstack((codes, code))
 84 | else:
 85 |     ids = np.array([database_vector_id])
 86 |     codes = np.array([code])
 87 |
 88 | write_ids_codes(ids, codes)
 89 |
 90 | """:py '2840581589434841'"""
 91 | # then at query time
 92 |
 93 | query_vector_float32 = np.random.rand(1, d).astype(np.float32)
 94 | index = faiss.IndexIDMap2(faiss.IndexLSH(d, nbits))
 95 | ids, codes = read_ids_codes()
 96 |
 97 | index.add_sa_codes(codes, ids)
 98 |
 99 | index.search(query_vector_float32, k=5)
100 |
101 | """:py"""
102 | !rm /tmp/ids.npy /tmp/codes.npy
103 |
104 | """:md
105 | ## IndexPQ: separate codes from codebook
106 |
107 | The second half of this notebook demonstrates how to separate serializing and deserializing the PQ codebook
108 |  (via faiss.write_index for IndexPQ) independently of the vector codes. For example, in the case
109 |  where you have a few vector embeddings per user and want to shard the flat index by user you
110 |  can re-use the same PQ method for all users but store each user's codes independently.
111 |
112 | """
113 |
114 | """:py"""
115 | M = d//8
116 | nbits = 8
117 |
118 | """:py"""
119 | # at train time
120 | template_index = faiss.index_factory(d, f"IDMap2,PQ{M}x{nbits}")
121 | template_index.train(training_data)
122 | write_template_index(template_index)
123 |
124 | """:py"""
125 | # New database vector
126 |
127 | index = read_template_index_instance()
128 | ids, codes = read_ids_codes()
129 | database_vector_id, database_vector_float32 = max(ids) + 1 if ids is not None else 1, np.random.rand(1, d).astype(np.float32)
130 |
131 | code = index.index.sa_encode(database_vector_float32)
132 |
133 | if ids is not None and codes is not None:
134 |     ids = np.concatenate((ids, [database_vector_id]))
135 |     codes = np.vstack((codes, code))
136 | else:
137 |     ids = np.array([database_vector_id])
138 |     codes = np.array([code])
139 |
140 | write_ids_codes(ids, codes)
141 |
142 | """:py '1858280061369209'"""
143 | # then at query time
144 | query_vector_float32 = np.random.rand(1, d).astype(np.float32)
145 | id_wrapper_index = read_template_index_instance()
146 | ids, codes = read_ids_codes()
147 |
148 | id_wrapper_index.add_sa_codes(codes, ids)
149 |
150 | id_wrapper_index.search(query_vector_float32, k=5)
151 |
152 | """:py"""
153 | !rm /tmp/ids.npy /tmp/codes.npy /tmp/template.index
154 |
155 | """:md
156 | ## Comparing these methods
157 |
158 | - methods: Flat, LSH, PQ
159 | - vary cost: nbits, M for 1x, 2x, 4x, 8x, 16x, 32x compression
160 | - measure: recall@1
161 |
162 | We don't measure latency as the number of vectors per user shard is insignificant.
163 |
164 | """
165 |
166 | """:py '2898032417027201'"""
167 | n, d
168 |
169 | """:py"""
170 | database_vector_ids, database_vector_float32s = np.arange(n), np.random.rand(n, d).astype(np.float32)
171 | query_vector_float32s = np.random.rand(n, d).astype(np.float32)
172 |
173 | """:py"""
174 | index = faiss.index_factory(d, "IDMap2,Flat")
175 | index.add_with_ids(database_vector_float32s, database_vector_ids)
176 | _, ground_truth_result_ids= index.search(query_vector_float32s, k=1)
177 |
178 | """:py '857475336204238'"""
179 | from dataclasses import dataclass
180 |
181 | pq_m_nbits = (
182 |     # 96 bytes
183 |     (96, 8),
184 |     (192, 4),
185 |     # 192 bytes
186 |     (192, 8),
187 |     (384, 4),
188 |     # 384 bytes
189 |     (384, 8),
190 |     (768, 4),
191 | )
192 | lsh_nbits = (768, 1536, 3072, 6144, 12288, 24576)
193 |
194 |
195 | @dataclass
196 | class Record:
197 |     type_: str
198 |     index: faiss.Index
199 |     args: tuple
200 |     recall: float
201 |
202 |
203 | results = []
204 |
205 | for m, nbits in pq_m_nbits:
206 |     print("pq", m, nbits)
207 |     index = faiss.index_factory(d, f"IDMap2,PQ{m}x{nbits}")
208 |     index.train(training_data)
209 |     index.add_with_ids(database_vector_float32s, database_vector_ids)
210 |     _, result_ids = index.search(query_vector_float32s, k=1)
211 |     recall = sum(result_ids == ground_truth_result_ids)
212 |     results.append(Record("pq", index, (m, nbits), recall))
213 |
214 | for nbits in lsh_nbits:
215 |     print("lsh", nbits)
216 |     index = faiss.IndexIDMap2(faiss.IndexLSH(d, nbits))
217 |     index.add_with_ids(database_vector_float32s, database_vector_ids)
218 |     _, result_ids = index.search(query_vector_float32s, k=1)
219 |     recall = sum(result_ids == ground_truth_result_ids)
220 |     results.append(Record("lsh", index, (nbits,), recall))
221 |
222 | """:py '556918346720794'"""
223 | import matplotlib.pyplot as plt
224 | import numpy as np
225 |
226 | def create_grouped_bar_chart(x_values, y_values_list, labels_list, xlabel, ylabel, title):
227 |     num_bars_per_group = len(x_values)
228 |
229 |     plt.figure(figsize=(12, 6))
230 |
231 |     for x, y_values, labels in zip(x_values, y_values_list, labels_list):
232 |         num_bars = len(y_values)
233 |         bar_width = 0.08 * x
234 |         bar_positions = np.arange(num_bars) * bar_width - (num_bars - 1) * bar_width / 2 + x
235 |
236 |         bars = plt.bar(bar_positions, y_values, width=bar_width)
237 |
238 |         for bar, label in zip(bars, labels):
239 |             height = bar.get_height()
240 |             plt.annotate(
241 |                 label,
242 |                 xy=(bar.get_x() + bar.get_width() / 2, height),
243 |                 xytext=(0, 3),
244 |                 textcoords="offset points",
245 |                 ha='center', va='bottom'
246 |             )
247 |
248 |     plt.xscale('log')
249 |     plt.xlabel(xlabel)
250 |     plt.ylabel(ylabel)
251 |     plt.title(title)
252 |     plt.xticks(x_values, labels=[str(x) for x in x_values])
253 |     plt.tight_layout()
254 |     plt.show()
255 |
256 | # # Example usage:
257 | # x_values = [1, 2, 4, 8, 16, 32]
258 | # y_values_list = [
259 | #     [2.5, 3.6, 1.8],
260 | #     [3.0, 2.8],
261 | #     [2.5, 3.5, 4.0, 1.0],
262 | #     [4.2],
263 | #     [3.0, 5.5, 2.2],
264 | #     [6.0, 4.5]
265 | # ]
266 | # labels_list = [
267 | #     ['A1', 'B1', 'C1'],
268 | #     ['A2', 'B2'],
269 | #     ['A3', 'B3', 'C3', 'D3'],
270 | #     ['A4'],
271 | #     ['A5', 'B5', 'C5'],
272 | #     ['A6', 'B6']
273 | # ]
274 |
275 | # create_grouped_bar_chart(x_values, y_values_list, labels_list, "x axis", "y axis", "title")
276 |
277 | """:py '1630106834206134'"""
278 | # x-axis: compression ratio
279 | # y-axis: recall@1
280 |
281 | from collections import defaultdict
282 |
283 | x = defaultdict(list)
284 | x[1].append(("flat", 1.00))
285 | for r in results:
286 |     y_value = r.recall[0] / n
287 |     x_value = int(d * 4 / r.index.sa_code_size())
288 |     label = None
289 |     if r.type_ == "pq":
290 |         label = f"PQ{r.args[0]}x{r.args[1]}"
291 |     if r.type_ == "lsh":
292 |         label = f"LSH{r.args[0]}"
293 |     x[x_value].append((label, y_value))
294 |
295 | x_values = sorted(list(x.keys()))
296 | create_grouped_bar_chart(
297 |     x_values,
298 |     [[e[1] for e in x[x_value]] for x_value in x_values],
299 |     [[e[0] for e in x[x_value]] for x_value in x_values],
300 |     "compression ratio",
301 |     "recall@1  q=1,000 queries",
302 |     "recall@1 for a database of n=1,000 d=768 vectors",
303 | )
304 |


--------------------------------------------------------------------------------
/demos/offline_ivf/__init__.py:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebookresearch/faiss/3d7659e46938f66b03bb5aac4d777012e383e0e7/demos/offline_ivf/__init__.py


--------------------------------------------------------------------------------
/demos/offline_ivf/create_sharded_ssnpp_files.py:
--------------------------------------------------------------------------------
 1 | # Copyright (c) Meta Platforms, Inc. and affiliates.
 2 | #
 3 | # This source code is licensed under the MIT license found in the
 4 | # LICENSE file in the root directory of this source tree.
 5 |
 6 | import numpy as np
 7 | import argparse
 8 | import os
 9 |
10 |
11 | def xbin_mmap(fname, dtype, maxn=-1):
12 |     """
13 |     Code from
14 |     https://github.com/harsha-simhadri/big-ann-benchmarks/blob/main/benchmark/dataset_io.py#L94
15 |     mmap the competition file format for a given type of items
16 |     """
17 |     n, d = map(int, np.fromfile(fname, dtype="uint32", count=2))
18 |     assert os.stat(fname).st_size == 8 + n * d * np.dtype(dtype).itemsize
19 |     if maxn > 0:
20 |         n = min(n, maxn)
21 |     return np.memmap(fname, dtype=dtype, mode="r", offset=8, shape=(n, d))
22 |
23 |
24 | def main(args: argparse.Namespace):
25 |     ssnpp_data = xbin_mmap(fname=args.filepath, dtype="uint8")
26 |     num_batches = ssnpp_data.shape[0] // args.data_batch
27 |     assert (
28 |         ssnpp_data.shape[0] % args.data_batch == 0
29 |     ), "num of embeddings per file should divide total num of embeddings"
30 |     for i in range(num_batches):
31 |         xb_batch = ssnpp_data[
32 |             i * args.data_batch:(i + 1) * args.data_batch, :
33 |         ]
34 |         filename = args.output_dir + f"/ssnpp_{(i):010}.npy"
35 |         np.save(filename, xb_batch)
36 |         print(f"File {filename} is saved!")
37 |
38 |
39 | if __name__ == "__main__":
40 |     parser = argparse.ArgumentParser()
41 |     parser.add_argument(
42 |         "--data_batch",
43 |         dest="data_batch",
44 |         type=int,
45 |         default=50000000,
46 |         help="Number of embeddings per file, should be a divisor of 1B",
47 |     )
48 |     parser.add_argument(
49 |         "--filepath",
50 |         dest="filepath",
51 |         type=str,
52 |         default="/datasets01/big-ann-challenge-data/FB_ssnpp/FB_ssnpp_database.u8bin",
53 |         help="path of 1B ssnpp database vectors' original file",
54 |     )
55 |     parser.add_argument(
56 |         "--filepath",
57 |         dest="output_dir",
58 |         type=str,
59 |         default="/checkpoint/marialomeli/ssnpp_data",
60 |         help="path to put sharded files",
61 |     )
62 |
63 |     args = parser.parse_args()
64 |     main(args)
65 |


--------------------------------------------------------------------------------
/demos/offline_ivf/dataset.py:
--------------------------------------------------------------------------------
  1 | # Copyright (c) Meta Platforms, Inc. and affiliates.
  2 | #
  3 | # This source code is licensed under the MIT license found in the
  4 | # LICENSE file in the root directory of this source tree.
  5 |
  6 | import os
  7 | import numpy as np
  8 | import faiss
  9 | from typing import List
 10 | import random
 11 | import logging
 12 | from functools import lru_cache
 13 |
 14 |
 15 | def create_dataset_from_oivf_config(cfg, ds_name):
 16 |     normalise = cfg["normalise"] if "normalise" in cfg else False
 17 |     return MultiFileVectorDataset(
 18 |         cfg["datasets"][ds_name]["root"],
 19 |         [
 20 |             FileDescriptor(
 21 |                 f["name"], f["format"], np.dtype(f["dtype"]), f["size"]
 22 |             )
 23 |             for f in cfg["datasets"][ds_name]["files"]
 24 |         ],
 25 |         cfg["d"],
 26 |         normalise,
 27 |         cfg["datasets"][ds_name]["size"],
 28 |     )
 29 |
 30 |
 31 | @lru_cache(maxsize=100)
 32 | def _memmap_vecs(
 33 |     file_name: str, format: str, dtype: np.dtype, size: int, d: int
 34 | ) -> np.array:
 35 |     """
 36 |     If the file is in raw format, the file size will
 37 |     be divisible by the dimensionality and by the size
 38 |     of the data type.
 39 |     Otherwise,the file contains a header and we assume
 40 |     it is of .npy type. It the returns the memmapped file.
 41 |     """
 42 |
 43 |     assert os.path.exists(file_name), f"file does not exist {file_name}"
 44 |     if format == "raw":
 45 |         fl = os.path.getsize(file_name)
 46 |         nb = fl // d // dtype.itemsize
 47 |         assert nb == size, f"{nb} is different than config's {size}"
 48 |         assert fl == d * dtype.itemsize * nb  # no header
 49 |         return np.memmap(file_name, shape=(nb, d), dtype=dtype, mode="r")
 50 |     elif format == "npy":
 51 |         vecs = np.load(file_name, mmap_mode="r")
 52 |         assert vecs.shape[0] == size, f"size:{size},shape {vecs.shape[0]}"
 53 |         assert vecs.shape[1] == d
 54 |         assert vecs.dtype == dtype
 55 |         return vecs
 56 |     else:
 57 |         ValueError("The file cannot be loaded in the current format.")
 58 |
 59 |
 60 | class FileDescriptor:
 61 |     def __init__(self, name: str, format: str, dtype: np.dtype, size: int):
 62 |         self.name = name
 63 |         self.format = format
 64 |         self.dtype = dtype
 65 |         self.size = size
 66 |
 67 |
 68 | class MultiFileVectorDataset:
 69 |     def __init__(
 70 |         self,
 71 |         root: str,
 72 |         file_descriptors: List[FileDescriptor],
 73 |         d: int,
 74 |         normalize: bool,
 75 |         size: int,
 76 |     ):
 77 |         assert os.path.exists(root)
 78 |         self.root = root
 79 |         self.file_descriptors = file_descriptors
 80 |         self.d = d
 81 |         self.normalize = normalize
 82 |         self.size = size
 83 |         self.file_offsets = [0]
 84 |         t = 0
 85 |         for f in self.file_descriptors:
 86 |             xb = _memmap_vecs(
 87 |                 f"{self.root}/{f.name}", f.format, f.dtype, f.size, self.d
 88 |             )
 89 |             t += xb.shape[0]
 90 |             self.file_offsets.append(t)
 91 |         assert (
 92 |             t == self.size
 93 |         ), "the sum of num of embeddings per file!=total num of embeddings"
 94 |
 95 |     def iterate(self, start: int, batch_size: int, dt: np.dtype):
 96 |         buffer = np.empty(shape=(batch_size, self.d), dtype=dt)
 97 |         rem = 0
 98 |         for f in self.file_descriptors:
 99 |             if start >= f.size:
100 |                 start -= f.size
101 |                 continue
102 |             logging.info(f"processing: {f.name}...")
103 |             xb = _memmap_vecs(
104 |                 f"{self.root}/{f.name}",
105 |                 f.format,
106 |                 f.dtype,
107 |                 f.size,
108 |                 self.d,
109 |             )
110 |             if start > 0:
111 |                 xb = xb[start:]
112 |                 start = 0
113 |             req = min(batch_size - rem, xb.shape[0])
114 |             buffer[rem:rem + req] = xb[:req]
115 |             rem += req
116 |             if rem == batch_size:
117 |                 if self.normalize:
118 |                     faiss.normalize_L2(buffer)
119 |                 yield buffer.copy()
120 |                 rem = 0
121 |             for i in range(req, xb.shape[0], batch_size):
122 |                 j = i + batch_size
123 |                 if j <= xb.shape[0]:
124 |                     tmp = xb[i:j].astype(dt)
125 |                     if self.normalize:
126 |                         faiss.normalize_L2(tmp)
127 |                     yield tmp
128 |                 else:
129 |                     rem = xb.shape[0] - i
130 |                     buffer[:rem] = xb[i:j]
131 |         if rem > 0:
132 |             tmp = buffer[:rem]
133 |             if self.normalize:
134 |                 faiss.normalize_L2(tmp)
135 |             yield tmp
136 |
137 |     def get(self, idx: List[int]):
138 |         n = len(idx)
139 |         fidx = np.searchsorted(self.file_offsets, idx, "right")
140 |         res = np.empty(shape=(len(idx), self.d), dtype=np.float32)
141 |         for r, id, fid in zip(range(n), idx, fidx):
142 |             assert fid > 0 and fid <= len(self.file_descriptors), f"{fid}"
143 |             f = self.file_descriptors[fid - 1]
144 |             # deferring normalization until after reading the vec
145 |             vecs = _memmap_vecs(
146 |                 f"{self.root}/{f.name}", f.format, f.dtype, f.size, self.d
147 |             )
148 |             i = id - self.file_offsets[fid - 1]
149 |             assert i >= 0 and i < vecs.shape[0]
150 |             res[r, :] = vecs[i]  # TODO: find a faster way
151 |         if self.normalize:
152 |             faiss.normalize_L2(res)
153 |         return res
154 |
155 |     def sample(self, n, idx_fn, vecs_fn):
156 |         if vecs_fn and os.path.exists(vecs_fn):
157 |             vecs = np.load(vecs_fn)
158 |             assert vecs.shape == (n, self.d)
159 |             return vecs
160 |         if idx_fn and os.path.exists(idx_fn):
161 |             idx = np.load(idx_fn)
162 |             assert idx.size == n
163 |         else:
164 |             idx = np.array(sorted(random.sample(range(self.size), n)))
165 |             if idx_fn:
166 |                 np.save(idx_fn, idx)
167 |         vecs = self.get(idx)
168 |         if vecs_fn:
169 |             np.save(vecs_fn, vecs)
170 |         return vecs
171 |
172 |     def get_first_n(self, n, dt):
173 |         assert n <= self.size
174 |         return next(self.iterate(0, n, dt))
175 |


--------------------------------------------------------------------------------
/demos/offline_ivf/generate_config.py:
--------------------------------------------------------------------------------
 1 | # Copyright (c) Meta Platforms, Inc. and affiliates.
 2 | #
 3 | # This source code is licensed under the MIT license found in the
 4 | # LICENSE file in the root directory of this source tree.
 5 |
 6 | import numpy as np
 7 | import os
 8 | import yaml
 9 |
10 | # with ssnpp sharded data
11 | root = "/checkpoint/marialomeli/ssnpp_data"
12 | file_names = [f"ssnpp_{i:010}.npy" for i in range(20)]
13 | d = 256
14 | dt = np.dtype(np.uint8)
15 |
16 |
17 | def read_embeddings(fp):
18 |     fl = os.path.getsize(fp)
19 |     nb = fl // d // dt.itemsize
20 |     print(nb)
21 |     if fl == d * dt.itemsize * nb:  # no header
22 |         return ("raw", np.memmap(fp, shape=(nb, d), dtype=dt, mode="r"))
23 |     else:  # assume npy
24 |         vecs = np.load(fp, mmap_mode="r")
25 |         assert vecs.shape[1] == d
26 |         assert vecs.dtype == dt
27 |         return ("npy", vecs)
28 |
29 |
30 | cfg = {}
31 | files = []
32 | size = 0
33 | for fn in file_names:
34 |     fp = f"{root}/{fn}"
35 |     assert os.path.exists(fp), f"{fp} is missing"
36 |     ft, xb = read_embeddings(fp)
37 |     files.append(
38 |         {"name": fn, "size": xb.shape[0], "dtype": dt.name, "format": ft}
39 |     )
40 |     size += xb.shape[0]
41 |
42 | cfg["size"] = size
43 | cfg["root"] = root
44 | cfg["d"] = d
45 | cfg["files"] = files
46 | print(yaml.dump(cfg))
47 |


--------------------------------------------------------------------------------
/demos/offline_ivf/offline_ivf.py:
--------------------------------------------------------------------------------
  1 | # Copyright (c) Meta Platforms, Inc. and affiliates.
  2 | #
  3 | # This source code is licensed under the MIT license found in the
  4 | # LICENSE file in the root directory of this source tree.
  5 |
  6 | import faiss
  7 | import numpy as np
  8 | import os
  9 | from tqdm import tqdm, trange
 10 | import sys
 11 | import logging
 12 | from faiss.contrib.ondisk import merge_ondisk
 13 | from faiss.contrib.big_batch_search import big_batch_search
 14 | from faiss.contrib.exhaustive_search import knn_ground_truth
 15 | from faiss.contrib.evaluation import knn_intersection_measure
 16 | from utils import (
 17 |     get_intersection_cardinality_frequencies,
 18 |     margin,
 19 |     is_pretransform_index,
 20 | )
 21 | from dataset import create_dataset_from_oivf_config
 22 |
 23 | logging.basicConfig(
 24 |     format=(
 25 |         "%(asctime)s.%(msecs)03d %(levelname)-8s %(threadName)-12s %(message)s"
 26 |     ),
 27 |     level=logging.INFO,
 28 |     datefmt="%Y-%m-%d %H:%M:%S",
 29 |     force=True,
 30 | )
 31 |
 32 | EMBEDDINGS_BATCH_SIZE: int = 100_000
 33 | NUM_SUBSAMPLES: int = 100
 34 | SMALL_DATA_SAMPLE: int = 10000
 35 |
 36 |
 37 | class OfflineIVF:
 38 |     def __init__(self, cfg, args, nprobe, index_factory_str):
 39 |         self.input_d = cfg["d"]
 40 |         self.dt = cfg["datasets"][args.xb]["files"][0]["dtype"]
 41 |         assert self.input_d > 0
 42 |         output_dir = cfg["output"]
 43 |         assert os.path.exists(output_dir)
 44 |         self.index_factory = index_factory_str
 45 |         assert self.index_factory is not None
 46 |         self.index_factory_fn = self.index_factory.replace(",", "_")
 47 |         self.index_template_file = (
 48 |             f"{output_dir}/{args.xb}/{self.index_factory_fn}.empty.faissindex"
 49 |         )
 50 |         logging.info(f"index template: {self.index_template_file}")
 51 |
 52 |         if not args.xq:
 53 |             args.xq = args.xb
 54 |
 55 |         self.by_residual = True
 56 |         if args.no_residuals:
 57 |             self.by_residual = False
 58 |
 59 |         xb_output_dir = f"{output_dir}/{args.xb}"
 60 |         if not os.path.exists(xb_output_dir):
 61 |             os.makedirs(xb_output_dir)
 62 |         xq_output_dir = f"{output_dir}/{args.xq}"
 63 |         if not os.path.exists(xq_output_dir):
 64 |             os.makedirs(xq_output_dir)
 65 |         search_output_dir = f"{output_dir}/{args.xq}_in_{args.xb}"
 66 |         if not os.path.exists(search_output_dir):
 67 |             os.makedirs(search_output_dir)
 68 |         self.knn_dir = f"{search_output_dir}/knn"
 69 |         if not os.path.exists(self.knn_dir):
 70 |             os.makedirs(self.knn_dir)
 71 |         self.eval_dir = f"{search_output_dir}/eval"
 72 |         if not os.path.exists(self.eval_dir):
 73 |             os.makedirs(self.eval_dir)
 74 |         self.index = {}  # to keep a reference to opened indices,
 75 |         self.ivls = {}  # hstack inverted lists,
 76 |         self.index_shards = {}  # and index shards
 77 |         self.index_shard_prefix = (
 78 |             f"{xb_output_dir}/{self.index_factory_fn}.shard_"
 79 |         )
 80 |         self.xq_index_shard_prefix = (
 81 |             f"{xq_output_dir}/{self.index_factory_fn}.shard_"
 82 |         )
 83 |         self.index_file = (  # TODO: added back temporarily for evaluate, handle name of non-sharded index file and remove.
 84 |             f"{xb_output_dir}/{self.index_factory_fn}.faissindex"
 85 |         )
 86 |         self.xq_index_file = (
 87 |             f"{xq_output_dir}/{self.index_factory_fn}.faissindex"
 88 |         )
 89 |         self.training_sample = cfg["training_sample"]
 90 |         self.evaluation_sample = cfg["evaluation_sample"]
 91 |         self.xq_ds = create_dataset_from_oivf_config(cfg, args.xq)
 92 |         self.xb_ds = create_dataset_from_oivf_config(cfg, args.xb)
 93 |         file_descriptors = self.xq_ds.file_descriptors
 94 |         self.file_sizes = [fd.size for fd in file_descriptors]
 95 |         self.shard_size = cfg["index_shard_size"]  # ~100GB
 96 |         self.nshards = self.xb_ds.size // self.shard_size
 97 |         if self.xb_ds.size % self.shard_size != 0:
 98 |             self.nshards += 1
 99 |         self.xq_nshards = self.xq_ds.size // self.shard_size
100 |         if self.xq_ds.size % self.shard_size != 0:
101 |             self.xq_nshards += 1
102 |         self.nprobe = nprobe
103 |         assert self.nprobe > 0, "Invalid nprobe parameter."
104 |         if "deduper" in cfg:
105 |             self.deduper = cfg["deduper"]
106 |             self.deduper_codec_fn = [
107 |                 f"{xb_output_dir}/deduper_codec_{codec.replace(',', '_')}"
108 |                 for codec in self.deduper
109 |             ]
110 |             self.deduper_idx_fn = [
111 |                 f"{xb_output_dir}/deduper_idx_{codec.replace(',', '_')}"
112 |                 for codec in self.deduper
113 |             ]
114 |         else:
115 |             self.deduper = None
116 |         self.k = cfg["k"]
117 |         assert self.k > 0, "Invalid number of neighbours parameter."
118 |         self.knn_output_file_suffix = (
119 |             f"{self.index_factory_fn}_np{self.nprobe}.npy"
120 |         )
121 |
122 |         fp = 32
123 |         if self.dt == "float16":
124 |             fp = 16
125 |
126 |         self.xq_bs = cfg["query_batch_size"]
127 |         if "metric" in cfg:
128 |             self.metric = eval(f'faiss.{cfg["metric"]}')
129 |         else:
130 |             self.metric = faiss.METRIC_L2
131 |
132 |         if "evaluate_by_margin" in cfg:
133 |             self.evaluate_by_margin = cfg["evaluate_by_margin"]
134 |         else:
135 |             self.evaluate_by_margin = False
136 |
137 |         os.system("grep -m1 'model name' < /proc/cpuinfo")
138 |         os.system("grep -E 'MemTotal|MemFree' /proc/meminfo")
139 |         os.system("nvidia-smi")
140 |         os.system("nvcc --version")
141 |
142 |         self.knn_queries_memory_limit = 4 * 1024 * 1024 * 1024  # 4 GB
143 |         self.knn_vectors_memory_limit = 8 * 1024 * 1024 * 1024  # 8 GB
144 |
145 |     def input_stats(self):
146 |         """
147 |         Trains the index using a subsample of the first chunk of data in the database and saves it in the template file (with no vectors added).
148 |         """
149 |         xb_sample = self.xb_ds.get_first_n(self.training_sample, np.float32)
150 |         logging.info(f"input shape: {xb_sample.shape}")
151 |         logging.info("running MatrixStats on training sample...")
152 |         logging.info(faiss.MatrixStats(xb_sample).comments)
153 |         logging.info("done")
154 |
155 |     def dedupe(self):
156 |         logging.info(self.deduper)
157 |         if self.deduper is None:
158 |             logging.info("No deduper configured")
159 |             return
160 |         codecs = []
161 |         codesets = []
162 |         idxs = []
163 |         for factory, filename in zip(self.deduper, self.deduper_codec_fn):
164 |             if os.path.exists(filename):
165 |                 logging.info(f"loading trained dedupe codec: {filename}")
166 |                 codec = faiss.read_index(filename)
167 |             else:
168 |                 logging.info(f"training dedupe codec: {factory}")
169 |                 codec = faiss.index_factory(self.input_d, factory)
170 |                 xb_sample = np.unique(
171 |                     self.xb_ds.get_first_n(100_000, np.float32), axis=0
172 |                 )
173 |                 faiss.ParameterSpace().set_index_parameter(codec, "verbose", 1)
174 |                 codec.train(xb_sample)
175 |                 logging.info(f"writing trained dedupe codec: {filename}")
176 |                 faiss.write_index(codec, filename)
177 |             codecs.append(codec)
178 |             codesets.append(faiss.CodeSet(codec.sa_code_size()))
179 |             idxs.append(np.empty((0,), dtype=np.uint32))
180 |         bs = 1_000_000
181 |         i = 0
182 |         for buffer in tqdm(self._iterate_transformed(self.xb_ds, 0, bs, np.float32)):
183 |             for j in range(len(codecs)):
184 |                 codec, codeset, idx = codecs[j], codesets[j], idxs[j]
185 |                 uniq = codeset.insert(codec.sa_encode(buffer))
186 |                 idxs[j] = np.append(
187 |                     idx,
188 |                     np.arange(i, i + buffer.shape[0], dtype=np.uint32)[uniq],
189 |                 )
190 |             i += buffer.shape[0]
191 |         for idx, filename in zip(idxs, self.deduper_idx_fn):
192 |             logging.info(f"writing {filename}, shape: {idx.shape}")
193 |             np.save(filename, idx)
194 |         logging.info("done")
195 |
196 |     def train_index(self):
197 |         """
198 |         Trains the index using a subsample of the first chunk of data in the database and saves it in the template file (with no vectors added).
199 |         """
200 |         assert not os.path.exists(self.index_template_file), (
201 |             "The train command has been ran, the index template file already"
202 |             " exists."
203 |         )
204 |         xb_sample = np.unique(
205 |             self.xb_ds.get_first_n(self.training_sample, np.float32), axis=0
206 |         )
207 |         logging.info(f"input shape: {xb_sample.shape}")
208 |         index = faiss.index_factory(
209 |             self.input_d, self.index_factory, self.metric
210 |         )
211 |         index_ivf = faiss.downcast_index(faiss.extract_index_ivf(index))
212 |         index_ivf.by_residual = True
213 |         faiss.ParameterSpace().set_index_parameter(index, "verbose", 1)
214 |         logging.info("running training...")
215 |         index.train(xb_sample)
216 |         logging.info(f"writing trained index {self.index_template_file}...")
217 |         faiss.write_index(index, self.index_template_file)
218 |         logging.info("done")
219 |
220 |     def _iterate_transformed(self, ds, start, batch_size, dt):
221 |         assert os.path.exists(self.index_template_file)
222 |         index = faiss.read_index(self.index_template_file)
223 |         if is_pretransform_index(index):
224 |             vt = index.chain.at(0)  # fetch pretransform
225 |             for buffer in ds.iterate(start, batch_size, dt):
226 |                 yield vt.apply(buffer)
227 |         else:
228 |             for buffer in ds.iterate(start, batch_size, dt):
229 |                 yield buffer
230 |
231 |     def index_shard(self):
232 |         assert os.path.exists(self.index_template_file)
233 |         index = faiss.read_index(self.index_template_file)
234 |         index_ivf = faiss.downcast_index(faiss.extract_index_ivf(index))
235 |         assert self.nprobe <= index_ivf.quantizer.ntotal, (
236 |             f"the number of vectors {index_ivf.quantizer.ntotal} is not enough"
237 |             f" to retrieve {self.nprobe} neighbours, check."
238 |         )
239 |         cpu_quantizer = index_ivf.quantizer
240 |         gpu_quantizer = faiss.index_cpu_to_all_gpus(cpu_quantizer)
241 |
242 |         for i in range(0, self.nshards):
243 |             sfn = f"{self.index_shard_prefix}{i}"
244 |             try:
245 |                 index.reset()
246 |                 index_ivf.quantizer = gpu_quantizer
247 |                 with open(sfn, "xb"):
248 |                     start = i * self.shard_size
249 |                     jj = 0
250 |                     embeddings_batch_size = min(
251 |                         EMBEDDINGS_BATCH_SIZE, self.shard_size
252 |                     )
253 |                     assert (
254 |                         self.shard_size % embeddings_batch_size == 0
255 |                         or EMBEDDINGS_BATCH_SIZE % embeddings_batch_size == 0
256 |                     ), (
257 |                         f"the shard size {self.shard_size} and embeddings"
258 |                         f" shard size  {EMBEDDINGS_BATCH_SIZE} are not"
259 |                         " divisible"
260 |                     )
261 |
262 |                     for xb_j in tqdm(
263 |                         self._iterate_transformed(
264 |                             self.xb_ds,
265 |                             start,
266 |                             embeddings_batch_size,
267 |                             np.float32,
268 |                         ),
269 |                         file=sys.stdout,
270 |                     ):
271 |                         if is_pretransform_index(index):
272 |                             assert xb_j.shape[1] == index.chain.at(0).d_out
273 |                             index_ivf.add_with_ids(
274 |                                 xb_j,
275 |                                 np.arange(start + jj, start + jj + xb_j.shape[0]),
276 |                             )
277 |                         else:
278 |                             assert xb_j.shape[1] == index.d
279 |                             index.add_with_ids(
280 |                                 xb_j,
281 |                                 np.arange(start + jj, start + jj + xb_j.shape[0]),
282 |                             )
283 |                         jj += xb_j.shape[0]
284 |                         logging.info(jj)
285 |                         assert (
286 |                             jj <= self.shard_size
287 |                         ), f"jj {jj} and shard_zide {self.shard_size}"
288 |                         if jj == self.shard_size:
289 |                             break
290 |                 logging.info(f"writing {sfn}...")
291 |                 index_ivf.quantizer = cpu_quantizer
292 |                 faiss.write_index(index, sfn)
293 |             except FileExistsError:
294 |                 logging.info(f"skipping shard: {i}")
295 |                 continue
296 |         logging.info("done")
297 |
298 |     def merge_index(self):
299 |         ivf_file = f"{self.index_file}.ivfdata"
300 |
301 |         assert os.path.exists(self.index_template_file)
302 |         assert not os.path.exists(
303 |             ivf_file
304 |         ), f"file with embeddings data {ivf_file} not found, check."
305 |         assert not os.path.exists(self.index_file)
306 |         index = faiss.read_index(self.index_template_file)
307 |         block_fnames = [
308 |             f"{self.index_shard_prefix}{i}" for i in range(self.nshards)
309 |         ]
310 |         for fn in block_fnames:
311 |             assert os.path.exists(fn)
312 |         logging.info(block_fnames)
313 |         logging.info("merging...")
314 |         merge_ondisk(index, block_fnames, ivf_file)
315 |         logging.info("writing index...")
316 |         faiss.write_index(index, self.index_file)
317 |         logging.info("done")
318 |
319 |     def _cached_search(
320 |         self,
321 |         sample,
322 |         xq_ds,
323 |         xb_ds,
324 |         idx_file,
325 |         vecs_file,
326 |         I_file,
327 |         D_file,
328 |         index_file=None,
329 |         nprobe=None,
330 |     ):
331 |         if not os.path.exists(I_file):
332 |             assert not os.path.exists(I_file), f"file {I_file} does not exist "
333 |             assert not os.path.exists(D_file), f"file {D_file} does not exist "
334 |             xq = xq_ds.sample(sample, idx_file, vecs_file)
335 |
336 |             if index_file:
337 |                 D, I = self._index_nonsharded_search(index_file, xq, nprobe)
338 |             else:
339 |                 logging.info("ground truth computations")
340 |                 db_iterator = xb_ds.iterate(0, 100_000, np.float32)
341 |                 D, I = knn_ground_truth(
342 |                     xq, db_iterator, self.k, metric_type=self.metric
343 |                 )
344 |                 assert np.amin(I) >= 0
345 |
346 |             np.save(I_file, I)
347 |             np.save(D_file, D)
348 |         else:
349 |             assert os.path.exists(idx_file), f"file {idx_file} does not exist "
350 |             assert os.path.exists(
351 |                 vecs_file
352 |             ), f"file {vecs_file} does not exist "
353 |             assert os.path.exists(I_file), f"file {I_file} does not exist "
354 |             assert os.path.exists(D_file), f"file {D_file} does not exist "
355 |             I = np.load(I_file)
356 |             D = np.load(D_file)
357 |         assert I.shape == (sample, self.k), f"{I_file} shape mismatch"
358 |         assert D.shape == (sample, self.k), f"{D_file} shape mismatch"
359 |         return (D, I)
360 |
361 |     def _index_search(self, index_shard_prefix, xq, nprobe):
362 |         assert nprobe is not None
363 |         logging.info(
364 |             f"open sharded index: {index_shard_prefix}, {self.nshards}"
365 |         )
366 |         index = self._open_sharded_index(index_shard_prefix)
367 |         index_ivf = faiss.downcast_index(faiss.extract_index_ivf(index))
368 |         logging.info(f"setting nprobe to {nprobe}")
369 |         index_ivf.nprobe = nprobe
370 |         return index.search(xq, self.k)
371 |
372 |     def _index_nonsharded_search(self, index_file, xq, nprobe):
373 |         assert nprobe is not None
374 |         logging.info(f"index {index_file}")
375 |         assert os.path.exists(index_file), f"file {index_file} does not exist "
376 |         index = faiss.read_index(index_file, faiss.IO_FLAG_ONDISK_SAME_DIR)
377 |         logging.info(f"index size {index.ntotal} ")
378 |         index_ivf = faiss.downcast_index(faiss.extract_index_ivf(index))
379 |         logging.info(f"setting nprobe to {nprobe}")
380 |         index_ivf.nprobe = nprobe
381 |         return index.search(xq, self.k)
382 |
383 |     def _refine_distances(self, xq_ds, idx, xb_ds, I):
384 |         xq = xq_ds.get(idx).repeat(self.k, axis=0)
385 |         xb = xb_ds.get(I.reshape(-1))
386 |         if self.metric == faiss.METRIC_INNER_PRODUCT:
387 |             return (xq * xb).sum(axis=1).reshape(I.shape)
388 |         elif self.metric == faiss.METRIC_L2:
389 |             return ((xq - xb) ** 2).sum(axis=1).reshape(I.shape)
390 |         else:
391 |             raise ValueError(f"metric not supported {self.metric}")
392 |
393 |     def evaluate(self):
394 |         self._evaluate(
395 |             self.index_factory_fn,
396 |             self.index_file,
397 |             self.xq_index_file,
398 |             self.nprobe,
399 |         )
400 |
401 |     def _evaluate(self, index_factory_fn, index_file, xq_index_file, nprobe):
402 |         idx_a_file = f"{self.eval_dir}/idx_a.npy"
403 |         idx_b_gt_file = f"{self.eval_dir}/idx_b_gt.npy"
404 |         idx_b_ann_file = (
405 |             f"{self.eval_dir}/idx_b_ann_{index_factory_fn}_np{nprobe}.npy"
406 |         )
407 |         vecs_a_file = f"{self.eval_dir}/vecs_a.npy"
408 |         vecs_b_gt_file = f"{self.eval_dir}/vecs_b_gt.npy"
409 |         vecs_b_ann_file = (
410 |             f"{self.eval_dir}/vecs_b_ann_{index_factory_fn}_np{nprobe}.npy"
411 |         )
412 |         D_a_gt_file = f"{self.eval_dir}/D_a_gt.npy"
413 |         D_a_ann_file = (
414 |             f"{self.eval_dir}/D_a_ann_{index_factory_fn}_np{nprobe}.npy"
415 |         )
416 |         D_a_ann_refined_file = f"{self.eval_dir}/D_a_ann_refined_{index_factory_fn}_np{nprobe}.npy"
417 |         D_b_gt_file = f"{self.eval_dir}/D_b_gt.npy"
418 |         D_b_ann_file = (
419 |             f"{self.eval_dir}/D_b_ann_{index_factory_fn}_np{nprobe}.npy"
420 |         )
421 |         D_b_ann_gt_file = (
422 |             f"{self.eval_dir}/D_b_ann_gt_{index_factory_fn}_np{nprobe}.npy"
423 |         )
424 |         I_a_gt_file = f"{self.eval_dir}/I_a_gt.npy"
425 |         I_a_ann_file = (
426 |             f"{self.eval_dir}/I_a_ann_{index_factory_fn}_np{nprobe}.npy"
427 |         )
428 |         I_b_gt_file = f"{self.eval_dir}/I_b_gt.npy"
429 |         I_b_ann_file = (
430 |             f"{self.eval_dir}/I_b_ann_{index_factory_fn}_np{nprobe}.npy"
431 |         )
432 |         I_b_ann_gt_file = (
433 |             f"{self.eval_dir}/I_b_ann_gt_{index_factory_fn}_np{nprobe}.npy"
434 |         )
435 |         margin_gt_file = f"{self.eval_dir}/margin_gt.npy"
436 |         margin_refined_file = (
437 |             f"{self.eval_dir}/margin_refined_{index_factory_fn}_np{nprobe}.npy"
438 |         )
439 |         margin_ann_file = (
440 |             f"{self.eval_dir}/margin_ann_{index_factory_fn}_np{nprobe}.npy"
441 |         )
442 |
443 |         logging.info("exact search forward")
444 |         # xq -> xb AKA a -> b
445 |         D_a_gt, I_a_gt = self._cached_search(
446 |             self.evaluation_sample,
447 |             self.xq_ds,
448 |             self.xb_ds,
449 |             idx_a_file,
450 |             vecs_a_file,
451 |             I_a_gt_file,
452 |             D_a_gt_file,
453 |         )
454 |         idx_a = np.load(idx_a_file)
455 |
456 |         logging.info("approximate search forward")
457 |         D_a_ann, I_a_ann = self._cached_search(
458 |             self.evaluation_sample,
459 |             self.xq_ds,
460 |             self.xb_ds,
461 |             idx_a_file,
462 |             vecs_a_file,
463 |             I_a_ann_file,
464 |             D_a_ann_file,
465 |             index_file,
466 |             nprobe,
467 |         )
468 |
469 |         logging.info(
470 |             "calculate refined distances on approximate search forward"
471 |         )
472 |         if os.path.exists(D_a_ann_refined_file):
473 |             D_a_ann_refined = np.load(D_a_ann_refined_file)
474 |             assert D_a_ann.shape == D_a_ann_refined.shape
475 |         else:
476 |             D_a_ann_refined = self._refine_distances(
477 |                 self.xq_ds, idx_a, self.xb_ds, I_a_ann
478 |             )
479 |             np.save(D_a_ann_refined_file, D_a_ann_refined)
480 |
481 |         if self.evaluate_by_margin:
482 |             k_extract = self.k
483 |             margin_threshold = 1.05
484 |             logging.info(
485 |                 "exact search backward from the k_extract NN results of"
486 |                 " forward search"
487 |             )
488 |             # xb -> xq AKA b -> a
489 |             D_a_b_gt = D_a_gt[:, :k_extract].ravel()
490 |             idx_b_gt = I_a_gt[:, :k_extract].ravel()
491 |             assert len(idx_b_gt) == self.evaluation_sample * k_extract
492 |             np.save(idx_b_gt_file, idx_b_gt)
493 |             # exact search
494 |             D_b_gt, _ = self._cached_search(
495 |                 len(idx_b_gt),
496 |                 self.xb_ds,
497 |                 self.xq_ds,
498 |                 idx_b_gt_file,
499 |                 vecs_b_gt_file,
500 |                 I_b_gt_file,
501 |                 D_b_gt_file,
502 |             )  # xb and xq ^^^ are inverted
503 |
504 |             logging.info("margin on exact search")
505 |             margin_gt = margin(
506 |                 self.evaluation_sample,
507 |                 idx_a,
508 |                 idx_b_gt,
509 |                 D_a_b_gt,
510 |                 D_a_gt,
511 |                 D_b_gt,
512 |                 self.k,
513 |                 k_extract,
514 |                 margin_threshold,
515 |             )
516 |             np.save(margin_gt_file, margin_gt)
517 |
518 |             logging.info(
519 |                 "exact search backward from the k_extract NN results of"
520 |                 " approximate forward search"
521 |             )
522 |             D_a_b_refined = D_a_ann_refined[:, :k_extract].ravel()
523 |             idx_b_ann = I_a_ann[:, :k_extract].ravel()
524 |             assert len(idx_b_ann) == self.evaluation_sample * k_extract
525 |             np.save(idx_b_ann_file, idx_b_ann)
526 |             # exact search
527 |             D_b_ann_gt, _ = self._cached_search(
528 |                 len(idx_b_ann),
529 |                 self.xb_ds,
530 |                 self.xq_ds,
531 |                 idx_b_ann_file,
532 |                 vecs_b_ann_file,
533 |                 I_b_ann_gt_file,
534 |                 D_b_ann_gt_file,
535 |             )  # xb and xq ^^^ are inverted
536 |
537 |             logging.info("refined margin on approximate search")
538 |             margin_refined = margin(
539 |                 self.evaluation_sample,
540 |                 idx_a,
541 |                 idx_b_ann,
542 |                 D_a_b_refined,
543 |                 D_a_gt,  # not D_a_ann_refined(!)
544 |                 D_b_ann_gt,
545 |                 self.k,
546 |                 k_extract,
547 |                 margin_threshold,
548 |             )
549 |             np.save(margin_refined_file, margin_refined)
550 |
551 |             D_b_ann, I_b_ann = self._cached_search(
552 |                 len(idx_b_ann),
553 |                 self.xb_ds,
554 |                 self.xq_ds,
555 |                 idx_b_ann_file,
556 |                 vecs_b_ann_file,
557 |                 I_b_ann_file,
558 |                 D_b_ann_file,
559 |                 xq_index_file,
560 |                 nprobe,
561 |             )
562 |
563 |             D_a_b_ann = D_a_ann[:, :k_extract].ravel()
564 |
565 |             logging.info("approximate search margin")
566 |
567 |             margin_ann = margin(
568 |                 self.evaluation_sample,
569 |                 idx_a,
570 |                 idx_b_ann,
571 |                 D_a_b_ann,
572 |                 D_a_ann,
573 |                 D_b_ann,
574 |                 self.k,
575 |                 k_extract,
576 |                 margin_threshold,
577 |             )
578 |             np.save(margin_ann_file, margin_ann)
579 |
580 |         logging.info("intersection")
581 |         logging.info(I_a_gt)
582 |         logging.info(I_a_ann)
583 |
584 |         for i in range(1, self.k + 1):
585 |             logging.info(
586 |                 f"{i}: {knn_intersection_measure(I_a_gt[:,:i], I_a_ann[:,:i])}"
587 |             )
588 |
589 |         logging.info(f"mean of gt distances: {D_a_gt.mean()}")
590 |         logging.info(f"mean of approx distances: {D_a_ann.mean()}")
591 |         logging.info(f"mean of refined distances: {D_a_ann_refined.mean()}")
592 |
593 |         logging.info("intersection cardinality frequencies")
594 |         logging.info(get_intersection_cardinality_frequencies(I_a_ann, I_a_gt))
595 |
596 |         logging.info("done")
597 |         pass
598 |
599 |     def _knn_function(self, xq, xb, k, metric, thread_id=None):
600 |         try:
601 |             return faiss.knn_gpu(
602 |                 self.all_gpu_resources[thread_id],
603 |                 xq,
604 |                 xb,
605 |                 k,
606 |                 metric=metric,
607 |                 device=thread_id,
608 |                 vectorsMemoryLimit=self.knn_vectors_memory_limit,
609 |                 queriesMemoryLimit=self.knn_queries_memory_limit,
610 |             )
611 |         except Exception:
612 |             logging.info(f"knn_function failed: {xq.shape}, {xb.shape}")
613 |             raise
614 |
615 |     def _coarse_quantize(self, index_ivf, xq, nprobe):
616 |         assert nprobe <= index_ivf.quantizer.ntotal
617 |         quantizer = faiss.index_cpu_to_all_gpus(index_ivf.quantizer)
618 |         bs = 100_000
619 |         nq = len(xq)
620 |         q_assign = np.empty((nq, nprobe), dtype="int32")
621 |         for i0 in trange(0, nq, bs):
622 |             i1 = min(nq, i0 + bs)
623 |             _, q_assign_i = quantizer.search(xq[i0:i1], nprobe)
624 |             q_assign[i0:i1] = q_assign_i
625 |         return q_assign
626 |
627 |     def search(self):
628 |         logging.info(f"search: {self.knn_dir}")
629 |         slurm_job_id = os.environ.get("SLURM_JOB_ID")
630 |
631 |         ngpu = faiss.get_num_gpus()
632 |         logging.info(f"number of gpus: {ngpu}")
633 |         self.all_gpu_resources = [
634 |             faiss.StandardGpuResources() for _ in range(ngpu)
635 |         ]
636 |         self._knn_function(
637 |             np.zeros((10, 10), dtype=np.float16),
638 |             np.zeros((10, 10), dtype=np.float16),
639 |             self.k,
640 |             metric=self.metric,
641 |             thread_id=0,
642 |         )
643 |
644 |         index = self._open_sharded_index()
645 |         index_ivf = faiss.downcast_index(faiss.extract_index_ivf(index))
646 |         logging.info(f"setting nprobe to {self.nprobe}")
647 |         index_ivf.nprobe = self.nprobe
648 |         # quantizer = faiss.index_cpu_to_all_gpus(index_ivf.quantizer)
649 |         for i in range(0, self.xq_ds.size, self.xq_bs):
650 |             Ifn = f"{self.knn_dir}/I{(i):010}_{self.knn_output_file_suffix}"
651 |             Dfn = f"{self.knn_dir}/D_approx{(i):010}_{self.knn_output_file_suffix}"
652 |             CPfn = f"{self.knn_dir}/CP{(i):010}_{self.knn_output_file_suffix}"
653 |
654 |             if slurm_job_id:
655 |                 worker_record = (
656 |                     self.knn_dir
657 |                     + f"/record_{(i):010}_{self.knn_output_file_suffix}.txt"
658 |                 )
659 |                 if not os.path.exists(worker_record):
660 |                     logging.info(
661 |                         f"creating record file {worker_record} and saving job"
662 |                         f" id: {slurm_job_id}"
663 |                     )
664 |                     with open(worker_record, "w") as h:
665 |                         h.write(slurm_job_id)
666 |                 else:
667 |                     old_slurm_id = open(worker_record, "r").read()
668 |                     logging.info(
669 |                         f"old job slurm id {old_slurm_id} and current job id:"
670 |                         f" {slurm_job_id}"
671 |                     )
672 |                     if old_slurm_id == slurm_job_id:
673 |                         if os.path.getsize(Ifn) == 0:
674 |                             logging.info(
675 |                                 f"cleaning up zero length files {Ifn} and"
676 |                                 f" {Dfn}"
677 |                             )
678 |                             os.remove(Ifn)
679 |                             os.remove(Dfn)
680 |
681 |             try:
682 |                 if is_pretransform_index(index):
683 |                     d = index.chain.at(0).d_out
684 |                 else:
685 |                     d = self.input_d
686 |                 with open(Ifn, "xb") as f, open(Dfn, "xb") as g:
687 |                     xq_i = np.empty(
688 |                         shape=(self.xq_bs, d), dtype=np.float16
689 |                     )
690 |                     q_assign = np.empty(
691 |                         (self.xq_bs, self.nprobe), dtype=np.int32
692 |                     )
693 |                     j = 0
694 |                     quantizer = faiss.index_cpu_to_all_gpus(
695 |                         index_ivf.quantizer
696 |                     )
697 |                     for xq_i_j in tqdm(
698 |                         self._iterate_transformed(
699 |                             self.xq_ds, i, min(100_000, self.xq_bs), np.float16
700 |                         ),
701 |                         file=sys.stdout,
702 |                     ):
703 |                         xq_i[j:j + xq_i_j.shape[0]] = xq_i_j
704 |                         (
705 |                             _,
706 |                             q_assign[j:j + xq_i_j.shape[0]],
707 |                         ) = quantizer.search(xq_i_j, self.nprobe)
708 |                         j += xq_i_j.shape[0]
709 |                         assert j <= xq_i.shape[0]
710 |                         if j == xq_i.shape[0]:
711 |                             break
712 |                     xq_i = xq_i[:j]
713 |                     q_assign = q_assign[:j]
714 |
715 |                     assert q_assign.shape == (xq_i.shape[0], index_ivf.nprobe)
716 |                     del quantizer
717 |                     logging.info(f"computing: {Ifn}")
718 |                     logging.info(f"computing: {Dfn}")
719 |                     prefetch_threads = faiss.get_num_gpus()
720 |                     D_ann, I = big_batch_search(
721 |                         index_ivf,
722 |                         xq_i,
723 |                         self.k,
724 |                         verbose=10,
725 |                         method="knn_function",
726 |                         knn=self._knn_function,
727 |                         threaded=faiss.get_num_gpus() * 8,
728 |                         use_float16=True,
729 |                         prefetch_threads=prefetch_threads,
730 |                         computation_threads=faiss.get_num_gpus(),
731 |                         q_assign=q_assign,
732 |                         checkpoint=CPfn,
733 |                         checkpoint_freq=7200,  # in seconds
734 |                     )
735 |                     assert (
736 |                         np.amin(I) >= 0
737 |                     ), f"{I}, there exists negative indices, check"
738 |                     logging.info(f"saving: {Ifn}")
739 |                     np.save(f, I)
740 |                     logging.info(f"saving: {Dfn}")
741 |                     np.save(g, D_ann)
742 |
743 |                     if os.path.exists(CPfn):
744 |                         logging.info(f"removing: {CPfn}")
745 |                         os.remove(CPfn)
746 |
747 |             except FileExistsError:
748 |                 logging.info(f"skipping {Ifn}, already exists")
749 |                 logging.info(f"skipping {Dfn}, already exists")
750 |                 continue
751 |
752 |     def _open_index_shard(self, fn):
753 |         if fn in self.index_shards:
754 |             index_shard = self.index_shards[fn]
755 |         else:
756 |             logging.info(f"open index shard: {fn}")
757 |             index_shard = faiss.read_index(
758 |                 fn, faiss.IO_FLAG_MMAP | faiss.IO_FLAG_READ_ONLY
759 |             )
760 |             self.index_shards[fn] = index_shard
761 |         return index_shard
762 |
763 |     def _open_sharded_index(self, index_shard_prefix=None):
764 |         if index_shard_prefix is None:
765 |             index_shard_prefix = self.index_shard_prefix
766 |         if index_shard_prefix in self.index:
767 |             return self.index[index_shard_prefix]
768 |         assert os.path.exists(
769 |             self.index_template_file
770 |         ), f"file {self.index_template_file} does not exist "
771 |         logging.info(f"open index template: {self.index_template_file}")
772 |         index = faiss.read_index(self.index_template_file)
773 |         index_ivf = faiss.downcast_index(faiss.extract_index_ivf(index))
774 |         ilv = faiss.InvertedListsPtrVector()
775 |         for i in range(self.nshards):
776 |             fn = f"{index_shard_prefix}{i}"
777 |             assert os.path.exists(fn), f"file {fn} does not exist "
778 |             logging.info(fn)
779 |             index_shard = self._open_index_shard(fn)
780 |             il = faiss.downcast_index(
781 |                 faiss.extract_index_ivf(index_shard)
782 |             ).invlists
783 |             ilv.push_back(il)
784 |         hsil = faiss.HStackInvertedLists(ilv.size(), ilv.data())
785 |         index_ivf.replace_invlists(hsil, False)
786 |         self.ivls[index_shard_prefix] = hsil
787 |         self.index[index_shard_prefix] = index
788 |         return index
789 |
790 |     def index_shard_stats(self):
791 |         for i in range(self.nshards):
792 |             fn = f"{self.index_shard_prefix}{i}"
793 |             assert os.path.exists(fn)
794 |             index = faiss.read_index(
795 |                 fn, faiss.IO_FLAG_MMAP | faiss.IO_FLAG_READ_ONLY
796 |             )
797 |             index_ivf = faiss.downcast_index(faiss.extract_index_ivf(index))
798 |             il = index_ivf.invlists
799 |             il.print_stats()
800 |
801 |     def index_stats(self):
802 |         index = self._open_sharded_index()
803 |         index_ivf = faiss.downcast_index(faiss.extract_index_ivf(index))
804 |         il = index_ivf.invlists
805 |         list_sizes = [il.list_size(i) for i in range(il.nlist)]
806 |         logging.info(np.max(list_sizes))
807 |         logging.info(np.mean(list_sizes))
808 |         logging.info(np.argmax(list_sizes))
809 |         logging.info("index_stats:")
810 |         il.print_stats()
811 |
812 |     def consistency_check(self):
813 |         logging.info("consistency-check")
814 |
815 |         logging.info("index template...")
816 |
817 |         assert os.path.exists(self.index_template_file)
818 |         index = faiss.read_index(self.index_template_file)
819 |
820 |         offset = 0  # 2**24
821 |         assert self.shard_size > offset + SMALL_DATA_SAMPLE
822 |
823 |         logging.info("index shards...")
824 |         for i in range(self.nshards):
825 |             r = i * self.shard_size + offset
826 |             xb = next(self.xb_ds.iterate(r, SMALL_DATA_SAMPLE, np.float32))
827 |             fn = f"{self.index_shard_prefix}{i}"
828 |             assert os.path.exists(fn), f"There is no index shard file {fn}"
829 |             index = self._open_index_shard(fn)
830 |             index_ivf = faiss.downcast_index(faiss.extract_index_ivf(index))
831 |             index_ivf.nprobe = 1
832 |             _, I = index.search(xb, 100)
833 |             for j in range(SMALL_DATA_SAMPLE):
834 |                 assert np.where(I[j] == j + r)[0].size > 0, (
835 |                     f"I[j]: {I[j]}, j: {j}, i: {i}, shard_size:"
836 |                     f" {self.shard_size}"
837 |                 )
838 |
839 |         logging.info("merged index...")
840 |         index = self._open_sharded_index()
841 |         index_ivf = faiss.downcast_index(faiss.extract_index_ivf(index))
842 |         index_ivf.nprobe = 1
843 |         for i in range(self.nshards):
844 |             r = i * self.shard_size + offset
845 |             xb = next(self.xb_ds.iterate(r, SMALL_DATA_SAMPLE, np.float32))
846 |             _, I = index.search(xb, 100)
847 |             for j in range(SMALL_DATA_SAMPLE):
848 |                 assert np.where(I[j] == j + r)[0].size > 0, (
849 |                     f"I[j]: {I[j]}, j: {j}, i: {i}, shard_size:"
850 |                     f" {self.shard_size}")
851 |
852 |         logging.info("search results...")
853 |         index_ivf.nprobe = self.nprobe
854 |         for i in range(0, self.xq_ds.size, self.xq_bs):
855 |             Ifn = f"{self.knn_dir}/I{i:010}_{self.index_factory_fn}_np{self.nprobe}.npy"
856 |             assert os.path.exists(Ifn)
857 |             assert os.path.getsize(Ifn) > 0, f"The file {Ifn} is empty."
858 |             logging.info(Ifn)
859 |             I = np.load(Ifn, mmap_mode="r")
860 |
861 |             assert I.shape[1] == self.k
862 |             assert I.shape[0] == min(self.xq_bs, self.xq_ds.size - i)
863 |             assert np.all(I[:, 1] >= 0)
864 |
865 |             Dfn = f"{self.knn_dir}/D_approx{i:010}_{self.index_factory_fn}_np{self.nprobe}.npy"
866 |             assert os.path.exists(Dfn)
867 |             assert os.path.getsize(Dfn) > 0, f"The file {Dfn} is empty."
868 |             logging.info(Dfn)
869 |             D = np.load(Dfn, mmap_mode="r")
870 |             assert D.shape == I.shape
871 |
872 |             xq = next(self.xq_ds.iterate(i, SMALL_DATA_SAMPLE, np.float32))
873 |             D_online, I_online = index.search(xq, self.k)
874 |             assert (
875 |                 np.where(I[:SMALL_DATA_SAMPLE] == I_online)[0].size
876 |                 / (self.k * SMALL_DATA_SAMPLE)
877 |                 > 0.95
878 |             ), (
879 |                 "the ratio is"
880 |                 f" {np.where(I[:SMALL_DATA_SAMPLE] == I_online)[0].size / (self.k * SMALL_DATA_SAMPLE)}"
881 |             )
882 |             assert np.allclose(
883 |                 D[:SMALL_DATA_SAMPLE].sum(axis=1),
884 |                 D_online.sum(axis=1),
885 |                 rtol=0.01,
886 |             ), (
887 |                 "the difference is"
888 |                 f" {D[:SMALL_DATA_SAMPLE].sum(axis=1), D_online.sum(axis=1)}"
889 |             )
890 |
891 |         logging.info("done")
892 |


--------------------------------------------------------------------------------
/demos/offline_ivf/run.py:
--------------------------------------------------------------------------------
  1 | # Copyright (c) Meta Platforms, Inc. and affiliates.
  2 | #
  3 | # This source code is licensed under the MIT license found in the
  4 | # LICENSE file in the root directory of this source tree.
  5 |
  6 | import argparse
  7 | from utils import (
  8 |     load_config,
  9 |     add_group_args,
 10 | )
 11 | from offline_ivf import OfflineIVF
 12 | import faiss
 13 | from typing import List, Callable, Dict
 14 | import submitit
 15 |
 16 |
 17 | def join_lists_in_dict(poss: List[str]) -> List[str]:
 18 |     """
 19 |     Joins two lists of prod and non-prod values, checking if the prod value is already included.
 20 |     If there is no non-prod list, it returns the prod list.
 21 |     """
 22 |     if "non-prod" in poss.keys():
 23 |         all_poss = poss["non-prod"]
 24 |         if poss["prod"][-1] not in poss["non-prod"]:
 25 |             all_poss += poss["prod"]
 26 |         return all_poss
 27 |     else:
 28 |         return poss["prod"]
 29 |
 30 |
 31 | def main(
 32 |     args: argparse.Namespace,
 33 |     cfg: Dict[str, str],
 34 |     nprobe: int,
 35 |     index_factory_str: str,
 36 | ) -> None:
 37 |     oivf = OfflineIVF(cfg, args, nprobe, index_factory_str)
 38 |     eval(f"oivf.{args.command}()")
 39 |
 40 |
 41 | def process_options_and_run_jobs(args: argparse.Namespace) -> None:
 42 |     """
 43 |     If "--cluster_run", it launches an array of jobs to the cluster using the submitit library for all the index strings. In
 44 |     the case of evaluate, it launches a job for each index string and nprobe pair. Otherwise, it launches a single job
 45 |     that is ran locally with the prod values for index string and nprobe.
 46 |     """
 47 |
 48 |     cfg = load_config(args.config)
 49 |     index_strings = cfg["index"]
 50 |     nprobes = cfg["nprobe"]
 51 |     if args.command == "evaluate":
 52 |         if args.cluster_run:
 53 |             all_nprobes = join_lists_in_dict(nprobes)
 54 |             all_index_strings = join_lists_in_dict(index_strings)
 55 |             for index_factory_str in all_index_strings:
 56 |                 for nprobe in all_nprobes:
 57 |                     launch_job(main, args, cfg, nprobe, index_factory_str)
 58 |         else:
 59 |             launch_job(
 60 |                 main, args, cfg, nprobes["prod"][-1], index_strings["prod"][-1]
 61 |             )
 62 |     else:
 63 |         if args.cluster_run:
 64 |             all_index_strings = join_lists_in_dict(index_strings)
 65 |             for index_factory_str in all_index_strings:
 66 |                 launch_job(
 67 |                     main, args, cfg, nprobes["prod"][-1], index_factory_str
 68 |                 )
 69 |         else:
 70 |             launch_job(
 71 |                 main, args, cfg, nprobes["prod"][-1], index_strings["prod"][-1]
 72 |             )
 73 |
 74 |
 75 | def launch_job(
 76 |     func: Callable,
 77 |     args: argparse.Namespace,
 78 |     cfg: Dict[str, str],
 79 |     n_probe: int,
 80 |     index_str: str,
 81 | ) -> None:
 82 |     """
 83 |     Launches an array of slurm jobs to the cluster using the submitit library.
 84 |     """
 85 |
 86 |     if args.cluster_run:
 87 |         assert args.num_nodes >= 1
 88 |         executor = submitit.AutoExecutor(folder=args.logs_dir)
 89 |
 90 |         executor.update_parameters(
 91 |             nodes=args.num_nodes,
 92 |             gpus_per_node=args.gpus_per_node,
 93 |             cpus_per_task=args.cpus_per_task,
 94 |             tasks_per_node=args.tasks_per_node,
 95 |             name=args.job_name,
 96 |             slurm_partition=args.partition,
 97 |             slurm_time=70 * 60,
 98 |         )
 99 |         if args.slurm_constraint:
100 |             executor.update_parameters(slurm_constraint=args.slurm_constrain)
101 |
102 |         job = executor.submit(func, args, cfg, n_probe, index_str)
103 |         print(f"Job id: {job.job_id}")
104 |     else:
105 |         func(args, cfg, n_probe, index_str)
106 |
107 |
108 | if __name__ == "__main__":
109 |     parser = argparse.ArgumentParser()
110 |     group = parser.add_argument_group("general")
111 |
112 |     add_group_args(group, "--command", required=True, help="command to run")
113 |     add_group_args(
114 |         group,
115 |         "--config",
116 |         required=True,
117 |         help="config yaml with the dataset specs",
118 |     )
119 |     add_group_args(
120 |         group, "--nt", type=int, default=96, help="nb search threads"
121 |     )
122 |     add_group_args(
123 |         group,
124 |         "--no_residuals",
125 |         action="store_false",
126 |         help="set index.by_residual to False during train index.",
127 |     )
128 |
129 |     group = parser.add_argument_group("slurm_job")
130 |
131 |     add_group_args(
132 |         group,
133 |         "--cluster_run",
134 |         action="store_true",
135 |         help=" if True, runs in cluster",
136 |     )
137 |     add_group_args(
138 |         group,
139 |         "--job_name",
140 |         type=str,
141 |         default="oivf",
142 |         help="cluster job name",
143 |     )
144 |     add_group_args(
145 |         group,
146 |         "--num_nodes",
147 |         type=str,
148 |         default=1,
149 |         help="num of nodes per job",
150 |     )
151 |     add_group_args(
152 |         group,
153 |         "--tasks_per_node",
154 |         type=int,
155 |         default=1,
156 |         help="tasks per job",
157 |     )
158 |
159 |     add_group_args(
160 |         group,
161 |         "--gpus_per_node",
162 |         type=int,
163 |         default=8,
164 |         help="cluster job name",
165 |     )
166 |     add_group_args(
167 |         group,
168 |         "--cpus_per_task",
169 |         type=int,
170 |         default=80,
171 |         help="cluster job name",
172 |     )
173 |
174 |     add_group_args(
175 |         group,
176 |         "--logs_dir",
177 |         type=str,
178 |         default="/checkpoint/marialomeli/offline_faiss/logs",
179 |         help="cluster job name",
180 |     )
181 |
182 |     add_group_args(
183 |         group,
184 |         "--slurm_constraint",
185 |         type=str,
186 |         default=None,
187 |         help="can be volta32gb for the fair cluster",
188 |     )
189 |
190 |     add_group_args(
191 |         group,
192 |         "--partition",
193 |         type=str,
194 |         default="learnlab",
195 |         help="specify which partition to use if ran on cluster with job arrays",
196 |         choices=[
197 |             "learnfair",
198 |             "devlab",
199 |             "scavenge",
200 |             "learnlab",
201 |             "nllb",
202 |             "seamless",
203 |             "seamless_medium",
204 |             "learnaccel",
205 |             "onellm_low",
206 |             "learn",
207 |             "scavenge",
208 |         ],
209 |     )
210 |
211 |     group = parser.add_argument_group("dataset")
212 |
213 |     add_group_args(group, "--xb", required=True, help="database vectors")
214 |     add_group_args(group, "--xq", help="query vectors")
215 |
216 |     args = parser.parse_args()
217 |     print("args:", args)
218 |     faiss.omp_set_num_threads(args.nt)
219 |     process_options_and_run_jobs(args=args)
220 |


--------------------------------------------------------------------------------
/demos/offline_ivf/tests/test_iterate_input.py:
--------------------------------------------------------------------------------
  1 | # Copyright (c) Meta Platforms, Inc. and affiliates.
  2 | #
  3 | # This source code is licensed under the MIT license found in the
  4 | # LICENSE file in the root directory of this source tree.
  5 |
  6 | import numpy as np
  7 | import unittest
  8 | from typing import List
  9 | from utils import load_config
 10 | from tests.testing_utils import TestDataCreator
 11 | import tempfile
 12 | from dataset import create_dataset_from_oivf_config
 13 |
 14 | DIMENSION: int = 768
 15 | SMALL_FILE_SIZES: List[int] = [100, 210, 450]
 16 | LARGE_FILE_SIZES: List[int] = [1253, 3459, 890]
 17 | TEST_BATCH_SIZE: int = 500
 18 | SMALL_SAMPLE_SIZE: int = 1000
 19 | NUM_FILES: int = 3
 20 |
 21 |
 22 | class TestUtilsMethods(unittest.TestCase):
 23 |     """
 24 |     Unit tests for iterate and decreasing_matrix methods.
 25 |     """
 26 |
 27 |     def test_iterate_input_file_smaller_than_batch(self):
 28 |         """
 29 |         Tests when batch size is larger than the file size.
 30 |         """
 31 |         with tempfile.TemporaryDirectory() as tmpdirname:
 32 |             data_creator = TestDataCreator(
 33 |                 tempdir=tmpdirname,
 34 |                 dimension=DIMENSION,
 35 |                 data_type=np.float16,
 36 |                 file_sizes=SMALL_FILE_SIZES,
 37 |             )
 38 |             data_creator.create_test_data()
 39 |             args = data_creator.setup_cli()
 40 |             cfg = load_config(args.config)
 41 |             db_iterator = create_dataset_from_oivf_config(
 42 |                 cfg, args.xb
 43 |             ).iterate(0, TEST_BATCH_SIZE, np.float32)
 44 |
 45 |             for i in range(len(SMALL_FILE_SIZES) - 1):
 46 |                 vecs = next(db_iterator)
 47 |                 if i != 1:
 48 |                     self.assertEqual(vecs.shape[0], TEST_BATCH_SIZE)
 49 |                 else:
 50 |                     self.assertEqual(
 51 |                         vecs.shape[0], sum(SMALL_FILE_SIZES) - TEST_BATCH_SIZE
 52 |                     )
 53 |
 54 |     def test_iterate_input_file_larger_than_batch(self):
 55 |         """
 56 |         Tests when batch size is smaller than the file size.
 57 |         """
 58 |         with tempfile.TemporaryDirectory() as tmpdirname:
 59 |             data_creator = TestDataCreator(
 60 |                 tempdir=tmpdirname,
 61 |                 dimension=DIMENSION,
 62 |                 data_type=np.float16,
 63 |                 file_sizes=LARGE_FILE_SIZES,
 64 |             )
 65 |             data_creator.create_test_data()
 66 |             args = data_creator.setup_cli()
 67 |             cfg = load_config(args.config)
 68 |             db_iterator = create_dataset_from_oivf_config(
 69 |                 cfg, args.xb
 70 |             ).iterate(0, TEST_BATCH_SIZE, np.float32)
 71 |
 72 |             for i in range(len(LARGE_FILE_SIZES) - 1):
 73 |                 vecs = next(db_iterator)
 74 |                 if i != 9:
 75 |                     self.assertEqual(vecs.shape[0], TEST_BATCH_SIZE)
 76 |                 else:
 77 |                     self.assertEqual(
 78 |                         vecs.shape[0],
 79 |                         sum(LARGE_FILE_SIZES) - TEST_BATCH_SIZE * 9,
 80 |                     )
 81 |
 82 |     def test_get_vs_iterate(self) -> None:
 83 |         """
 84 |         Loads vectors with iterator and get, and checks that they match, non-aligned by file size case.
 85 |         """
 86 |         with tempfile.TemporaryDirectory() as tmpdirname:
 87 |             data_creator = TestDataCreator(
 88 |                 tempdir=tmpdirname,
 89 |                 dimension=DIMENSION,
 90 |                 data_type=np.float16,
 91 |                 file_size=SMALL_SAMPLE_SIZE,
 92 |                 num_files=NUM_FILES,
 93 |                 normalise=True,
 94 |             )
 95 |             data_creator.create_test_data()
 96 |             args = data_creator.setup_cli()
 97 |             cfg = load_config(args.config)
 98 |             ds = create_dataset_from_oivf_config(cfg, args.xb)
 99 |             vecs_by_iterator = np.vstack(list(ds.iterate(0, 317, np.float32)))
100 |             self.assertEqual(
101 |                 vecs_by_iterator.shape[0], SMALL_SAMPLE_SIZE * NUM_FILES
102 |             )
103 |             vecs_by_get = ds.get(list(range(vecs_by_iterator.shape[0])))
104 |             self.assertTrue(np.all(vecs_by_iterator == vecs_by_get))
105 |
106 |     def test_iterate_back(self) -> None:
107 |         """
108 |         Loads vectors with iterator and get, and checks that they match, non-aligned by file size case.
109 |         """
110 |         with tempfile.TemporaryDirectory() as tmpdirname:
111 |             data_creator = TestDataCreator(
112 |                 tempdir=tmpdirname,
113 |                 dimension=DIMENSION,
114 |                 data_type=np.float16,
115 |                 file_size=SMALL_SAMPLE_SIZE,
116 |                 num_files=NUM_FILES,
117 |                 normalise=True,
118 |             )
119 |             data_creator.create_test_data()
120 |             args = data_creator.setup_cli()
121 |             cfg = load_config(args.config)
122 |             ds = create_dataset_from_oivf_config(cfg, args.xb)
123 |             vecs_by_iterator = np.vstack(list(ds.iterate(0, 317, np.float32)))
124 |             self.assertEqual(
125 |                 vecs_by_iterator.shape[0], SMALL_SAMPLE_SIZE * NUM_FILES
126 |             )
127 |             vecs_chunk = np.vstack(
128 |                 [
129 |                     next(ds.iterate(i, 543, np.float32))
130 |                     for i in range(0, SMALL_SAMPLE_SIZE * NUM_FILES, 543)
131 |                 ]
132 |             )
133 |             self.assertTrue(np.all(vecs_by_iterator == vecs_chunk))
134 |


--------------------------------------------------------------------------------
/demos/offline_ivf/tests/test_offline_ivf.py:
--------------------------------------------------------------------------------
  1 | # Copyright (c) Meta Platforms, Inc. and affiliates.
  2 | #
  3 | # This source code is licensed under the MIT license found in the
  4 | # LICENSE file in the root directory of this source tree.
  5 |
  6 | import numpy as np
  7 | import unittest
  8 | from utils import load_config
  9 | import pathlib as pl
 10 | import tempfile
 11 | from typing import List
 12 | from tests.testing_utils import TestDataCreator
 13 | from run import process_options_and_run_jobs
 14 |
 15 | KNN_RESULTS_FILE: str = (
 16 |     "/my_test_data_in_my_test_data/knn/I0000000000_IVF256_PQ4_np2.npy"
 17 | )
 18 |
 19 | A_INDEX_FILES: List[str] = [
 20 |     "I_a_gt.npy",
 21 |     "D_a_gt.npy",
 22 |     "vecs_a.npy",
 23 |     "D_a_ann_IVF256_PQ4_np2.npy",
 24 |     "I_a_ann_IVF256_PQ4_np2.npy",
 25 |     "D_a_ann_refined_IVF256_PQ4_np2.npy",
 26 | ]
 27 |
 28 | A_INDEX_OPQ_FILES: List[str] = [
 29 |     "I_a_gt.npy",
 30 |     "D_a_gt.npy",
 31 |     "vecs_a.npy",
 32 |     "D_a_ann_OPQ4_IVF256_PQ4_np200.npy",
 33 |     "I_a_ann_OPQ4_IVF256_PQ4_np200.npy",
 34 |     "D_a_ann_refined_OPQ4_IVF256_PQ4_np200.npy",
 35 | ]
 36 |
 37 |
 38 | class TestOIVF(unittest.TestCase):
 39 |     """
 40 |     Unit tests for OIVF. Some of these unit tests first copy the required test data objects and puts them in the tempdir created by the context manager.
 41 |     """
 42 |
 43 |     def assert_file_exists(self, filepath: str) -> None:
 44 |         path = pl.Path(filepath)
 45 |         self.assertEqual((str(path), path.is_file()), (str(path), True))
 46 |
 47 |     def test_consistency_check(self) -> None:
 48 |         """
 49 |         Test the OIVF consistency check step, that it throws if no other steps have been ran.
 50 |         """
 51 |         with tempfile.TemporaryDirectory() as tmpdirname:
 52 |             data_creator = TestDataCreator(
 53 |                 tempdir=tmpdirname,
 54 |                 dimension=8,
 55 |                 data_type=np.float16,
 56 |                 index_factory=["OPQ4,IVF256,PQ4"],
 57 |                 training_sample=9984,
 58 |                 num_files=3,
 59 |                 file_size=10000,
 60 |                 nprobe=2,
 61 |                 k=2,
 62 |                 metric="METRIC_L2",
 63 |             )
 64 |             data_creator.create_test_data()
 65 |             test_args = data_creator.setup_cli("consistency_check")
 66 |             self.assertRaises(
 67 |                 AssertionError, process_options_and_run_jobs, test_args
 68 |             )
 69 |
 70 |     def test_train_index(self) -> None:
 71 |         """
 72 |         Test the OIVF train index step, that it correctly produces the empty.faissindex template file.
 73 |         """
 74 |         with tempfile.TemporaryDirectory() as tmpdirname:
 75 |             data_creator = TestDataCreator(
 76 |                 tempdir=tmpdirname,
 77 |                 dimension=8,
 78 |                 data_type=np.float16,
 79 |                 index_factory=["OPQ4,IVF256,PQ4"],
 80 |                 training_sample=9984,
 81 |                 num_files=3,
 82 |                 file_size=10000,
 83 |                 nprobe=2,
 84 |                 k=2,
 85 |                 metric="METRIC_L2",
 86 |             )
 87 |             data_creator.create_test_data()
 88 |             test_args = data_creator.setup_cli("train_index")
 89 |             cfg = load_config(test_args.config)
 90 |             process_options_and_run_jobs(test_args)
 91 |             empty_index = (
 92 |                 cfg["output"]
 93 |                 + "/my_test_data/"
 94 |                 + cfg["index"]["prod"][-1].replace(",", "_")
 95 |                 + ".empty.faissindex"
 96 |             )
 97 |             self.assert_file_exists(empty_index)
 98 |
 99 |     def test_index_shard_equal_file_sizes(self) -> None:
100 |         """
101 |         Test the case where the shard size is a divisor of the database size and it is equal to the first file size.
102 |         """
103 |
104 |         with tempfile.TemporaryDirectory() as tmpdirname:
105 |             index_shard_size = 10000
106 |             num_files = 3
107 |             file_size = 10000
108 |             xb_ds_size = num_files * file_size
109 |             data_creator = TestDataCreator(
110 |                 tempdir=tmpdirname,
111 |                 dimension=8,
112 |                 data_type=np.float16,
113 |                 index_factory=["IVF256,PQ4"],
114 |                 training_sample=9984,
115 |                 num_files=num_files,
116 |                 file_size=file_size,
117 |                 nprobe=2,
118 |                 k=2,
119 |                 metric="METRIC_L2",
120 |                 index_shard_size=index_shard_size,
121 |                 query_batch_size=1000,
122 |                 evaluation_sample=100,
123 |             )
124 |             data_creator.create_test_data()
125 |             test_args = data_creator.setup_cli("train_index")
126 |             process_options_and_run_jobs(test_args)
127 |             test_args = data_creator.setup_cli("index_shard")
128 |             cfg = load_config(test_args.config)
129 |             process_options_and_run_jobs(test_args)
130 |             num_shards = xb_ds_size // index_shard_size
131 |             if xb_ds_size % index_shard_size != 0:
132 |                 num_shards += 1
133 |             print(f"number of shards:{num_shards}")
134 |             for i in range(num_shards):
135 |                 index_shard_file = (
136 |                     cfg["output"]
137 |                     + "/my_test_data/"
138 |                     + cfg["index"]["prod"][-1].replace(",", "_")
139 |                     + f".shard_{i}"
140 |                 )
141 |                 self.assert_file_exists(index_shard_file)
142 |
143 |     def test_index_shard_unequal_file_sizes(self) -> None:
144 |         """
145 |         Test the case where the shard size is not a divisor of the database size and is greater than the first file size.
146 |         """
147 |         with tempfile.TemporaryDirectory() as tmpdirname:
148 |             file_sizes = [20000, 15001, 13990]
149 |             xb_ds_size = sum(file_sizes)
150 |             index_shard_size = 30000
151 |             data_creator = TestDataCreator(
152 |                 tempdir=tmpdirname,
153 |                 dimension=8,
154 |                 data_type=np.float16,
155 |                 index_factory=["IVF256,PQ4"],
156 |                 training_sample=9984,
157 |                 file_sizes=file_sizes,
158 |                 nprobe=2,
159 |                 k=2,
160 |                 metric="METRIC_L2",
161 |                 index_shard_size=index_shard_size,
162 |                 evaluation_sample=100,
163 |             )
164 |             data_creator.create_test_data()
165 |             test_args = data_creator.setup_cli("train_index")
166 |             process_options_and_run_jobs(test_args)
167 |             test_args = data_creator.setup_cli("index_shard")
168 |             cfg = load_config(test_args.config)
169 |             process_options_and_run_jobs(test_args)
170 |             num_shards = xb_ds_size // index_shard_size
171 |             if xb_ds_size % index_shard_size != 0:
172 |                 num_shards += 1
173 |             print(f"number of shards:{num_shards}")
174 |             for i in range(num_shards):
175 |                 index_shard_file = (
176 |                     cfg["output"]
177 |                     + "/my_test_data/"
178 |                     + cfg["index"]["prod"][-1].replace(",", "_")
179 |                     + f".shard_{i}"
180 |                 )
181 |                 self.assert_file_exists(index_shard_file)
182 |
183 |     def test_search(self) -> None:
184 |         """
185 |         Test search step using test data objects to bypass dependencies on previous steps.
186 |         """
187 |         with tempfile.TemporaryDirectory() as tmpdirname:
188 |             num_files = 3
189 |             file_size = 10000
190 |             query_batch_size = 10000
191 |             total_batches = num_files * file_size // query_batch_size
192 |             if num_files * file_size % query_batch_size != 0:
193 |                 total_batches += 1
194 |             data_creator = TestDataCreator(
195 |                 tempdir=tmpdirname,
196 |                 dimension=8,
197 |                 data_type=np.float32,
198 |                 index_factory=["IVF256,PQ4"],
199 |                 training_sample=9984,
200 |                 num_files=3,
201 |                 file_size=10000,
202 |                 nprobe=2,
203 |                 k=2,
204 |                 metric="METRIC_L2",
205 |                 index_shard_size=10000,
206 |                 query_batch_size=query_batch_size,
207 |                 evaluation_sample=100,
208 |             )
209 |             data_creator.create_test_data()
210 |             test_args = data_creator.setup_cli("train_index")
211 |             process_options_and_run_jobs(test_args)
212 |             test_args = data_creator.setup_cli("index_shard")
213 |             process_options_and_run_jobs(test_args)
214 |             test_args = data_creator.setup_cli("search")
215 |             cfg = load_config(test_args.config)
216 |             process_options_and_run_jobs(test_args)
217 |             # TODO: add check that there are number of batches total of files
218 |             knn_file = cfg["output"] + KNN_RESULTS_FILE
219 |             self.assert_file_exists(knn_file)
220 |
221 |     def test_evaluate_without_margin(self) -> None:
222 |         """
223 |         Test evaluate step using test data objects, no margin evaluation, single index.
224 |         """
225 |         with tempfile.TemporaryDirectory() as tmpdirname:
226 |             data_creator = TestDataCreator(
227 |                 tempdir=tmpdirname,
228 |                 dimension=8,
229 |                 data_type=np.float32,
230 |                 index_factory=["IVF256,PQ4"],
231 |                 training_sample=9984,
232 |                 num_files=3,
233 |                 file_size=10000,
234 |                 nprobe=2,
235 |                 k=2,
236 |                 metric="METRIC_L2",
237 |                 index_shard_size=10000,
238 |                 query_batch_size=10000,
239 |                 evaluation_sample=100,
240 |                 with_queries_ds=True,
241 |             )
242 |             data_creator.create_test_data()
243 |             test_args = data_creator.setup_cli("train_index")
244 |             process_options_and_run_jobs(test_args)
245 |             test_args = data_creator.setup_cli("index_shard")
246 |             process_options_and_run_jobs(test_args)
247 |             test_args = data_creator.setup_cli("merge_index")
248 |             process_options_and_run_jobs(test_args)
249 |             test_args = data_creator.setup_cli("evaluate")
250 |             process_options_and_run_jobs(test_args)
251 |             common_path = tmpdirname + "/my_queries_data_in_my_test_data/eval/"
252 |             for filename in A_INDEX_FILES:
253 |                 file_to_check = common_path + "/" + filename
254 |                 self.assert_file_exists(file_to_check)
255 |
256 |     def test_evaluate_without_margin_OPQ(self) -> None:
257 |         """
258 |         Test evaluate step using test data objects, no margin evaluation, single index.
259 |         """
260 |         with tempfile.TemporaryDirectory() as tmpdirname:
261 |             data_creator = TestDataCreator(
262 |                 tempdir=tmpdirname,
263 |                 dimension=8,
264 |                 data_type=np.float32,
265 |                 index_factory=["OPQ4,IVF256,PQ4"],
266 |                 training_sample=9984,
267 |                 num_files=3,
268 |                 file_size=10000,
269 |                 nprobe=200,
270 |                 k=2,
271 |                 metric="METRIC_L2",
272 |                 index_shard_size=10000,
273 |                 query_batch_size=10000,
274 |                 evaluation_sample=100,
275 |                 with_queries_ds=True,
276 |             )
277 |             data_creator.create_test_data()
278 |             test_args = data_creator.setup_cli("train_index")
279 |             process_options_and_run_jobs(test_args)
280 |             test_args = data_creator.setup_cli("index_shard")
281 |             process_options_and_run_jobs(test_args)
282 |             test_args = data_creator.setup_cli("merge_index")
283 |             process_options_and_run_jobs(test_args)
284 |             test_args = data_creator.setup_cli("evaluate")
285 |             process_options_and_run_jobs(test_args)
286 |             common_path = tmpdirname + "/my_queries_data_in_my_test_data/eval/"
287 |             for filename in A_INDEX_OPQ_FILES:
288 |                 file_to_check = common_path + filename
289 |                 self.assert_file_exists(file_to_check)
290 |


--------------------------------------------------------------------------------
/demos/offline_ivf/tests/testing_utils.py:
--------------------------------------------------------------------------------
  1 | # Copyright (c) Meta Platforms, Inc. and affiliates.
  2 | #
  3 | # This source code is licensed under the MIT license found in the
  4 | # LICENSE file in the root directory of this source tree.
  5 |
  6 | import argparse
  7 | import yaml
  8 | import numpy as np
  9 | from typing import Dict, List, Optional
 10 |
 11 | OIVF_TEST_ARGS: List[str] = [
 12 |     "--config",
 13 |     "--xb",
 14 |     "--xq",
 15 |     "--command",
 16 |     "--cluster_run",
 17 |     "--no_residuals",
 18 | ]
 19 |
 20 |
 21 | def get_test_parser(args) -> argparse.ArgumentParser:
 22 |     parser = argparse.ArgumentParser()
 23 |     for arg in args:
 24 |         parser.add_argument(arg)
 25 |     return parser
 26 |
 27 |
 28 | class TestDataCreator:
 29 |     def __init__(
 30 |         self,
 31 |         tempdir: str,
 32 |         dimension: int,
 33 |         data_type: np.dtype,
 34 |         index_factory: Optional[List] = ["OPQ4,IVF256,PQ4"],
 35 |         training_sample: Optional[int] = 9984,
 36 |         index_shard_size: Optional[int] = 1000,
 37 |         query_batch_size: Optional[int] = 1000,
 38 |         evaluation_sample: Optional[int] = 100,
 39 |         num_files: Optional[int] = None,
 40 |         file_size: Optional[int] = None,
 41 |         file_sizes: Optional[List] = None,
 42 |         nprobe: Optional[int] = 64,
 43 |         k: Optional[int] = 10,
 44 |         metric: Optional[str] = "METRIC_L2",
 45 |         normalise: Optional[bool] = False,
 46 |         with_queries_ds: Optional[bool] = False,
 47 |         evaluate_by_margin: Optional[bool] = False,
 48 |     ) -> None:
 49 |         self.tempdir = tempdir
 50 |         self.dimension = dimension
 51 |         self.data_type = np.dtype(data_type).name
 52 |         self.index_factory = {"prod": index_factory}
 53 |         if file_size and num_files:
 54 |             self.file_sizes = [file_size for _ in range(num_files)]
 55 |         elif file_sizes:
 56 |             self.file_sizes = file_sizes
 57 |         else:
 58 |             raise ValueError("no file sizes provided")
 59 |         self.num_files = len(self.file_sizes)
 60 |         self.training_sample = training_sample
 61 |         self.index_shard_size = index_shard_size
 62 |         self.query_batch_size = query_batch_size
 63 |         self.evaluation_sample = evaluation_sample
 64 |         self.nprobe = {"prod": [nprobe]}
 65 |         self.k = k
 66 |         self.metric = metric
 67 |         self.normalise = normalise
 68 |         self.config_file = self.tempdir + "/config_test.yaml"
 69 |         self.ds_name = "my_test_data"
 70 |         self.qs_name = "my_queries_data"
 71 |         self.evaluate_by_margin = evaluate_by_margin
 72 |         self.with_queries_ds = with_queries_ds
 73 |
 74 |     def create_test_data(self) -> None:
 75 |         datafiles = self._create_data_files()
 76 |         files_info = []
 77 |
 78 |         for i, file in enumerate(datafiles):
 79 |             files_info.append(
 80 |                 {
 81 |                     "dtype": self.data_type,
 82 |                     "format": "npy",
 83 |                     "name": file,
 84 |                     "size": self.file_sizes[i],
 85 |                 }
 86 |             )
 87 |
 88 |         config_for_yaml = {
 89 |             "d": self.dimension,
 90 |             "output": self.tempdir,
 91 |             "index": self.index_factory,
 92 |             "nprobe": self.nprobe,
 93 |             "k": self.k,
 94 |             "normalise": self.normalise,
 95 |             "metric": self.metric,
 96 |             "training_sample": self.training_sample,
 97 |             "evaluation_sample": self.evaluation_sample,
 98 |             "index_shard_size": self.index_shard_size,
 99 |             "query_batch_size": self.query_batch_size,
100 |             "datasets": {
101 |                 self.ds_name: {
102 |                     "root": self.tempdir,
103 |                     "size": sum(self.file_sizes),
104 |                     "files": files_info,
105 |                 }
106 |             },
107 |         }
108 |         if self.evaluate_by_margin:
109 |             config_for_yaml["evaluate_by_margin"] = self.evaluate_by_margin
110 |         q_datafiles = self._create_data_files("my_q_data")
111 |         q_files_info = []
112 |
113 |         for i, file in enumerate(q_datafiles):
114 |             q_files_info.append(
115 |                 {
116 |                     "dtype": self.data_type,
117 |                     "format": "npy",
118 |                     "name": file,
119 |                     "size": self.file_sizes[i],
120 |                 }
121 |             )
122 |         if self.with_queries_ds:
123 |             config_for_yaml["datasets"][self.qs_name] = {
124 |                 "root": self.tempdir,
125 |                 "size": sum(self.file_sizes),
126 |                 "files": q_files_info,
127 |             }
128 |
129 |         self._create_config_yaml(config_for_yaml)
130 |
131 |     def setup_cli(self, command="consistency_check") -> argparse.Namespace:
132 |         parser = get_test_parser(OIVF_TEST_ARGS)
133 |
134 |         if self.with_queries_ds:
135 |             return parser.parse_args(
136 |                 [
137 |                     "--xb",
138 |                     self.ds_name,
139 |                     "--config",
140 |                     self.config_file,
141 |                     "--command",
142 |                     command,
143 |                     "--xq",
144 |                     self.qs_name,
145 |                 ]
146 |             )
147 |         return parser.parse_args(
148 |             [
149 |                 "--xb",
150 |                 self.ds_name,
151 |                 "--config",
152 |                 self.config_file,
153 |                 "--command",
154 |                 command,
155 |             ]
156 |         )
157 |
158 |     def _create_data_files(self, name_of_file="my_data") -> List[str]:
159 |         """
160 |         Creates a dataset "my_test_data" with number of files (num_files), using padding in the files
161 |         name. If self.with_queries is True, it adds an extra dataset "my_queries_data" with the same number of files
162 |         as the "my_test_data". The default name for embeddings files is "my_data" + <padding>.npy.
163 |         """
164 |         filenames = []
165 |         for i, file_size in enumerate(self.file_sizes):
166 |             # np.random.seed(i)
167 |             db_vectors = np.random.random((file_size, self.dimension)).astype(
168 |                 self.data_type
169 |             )
170 |             filename = name_of_file + f"{i:02}" + ".npy"
171 |             filenames.append(filename)
172 |             np.save(self.tempdir + "/" + filename, db_vectors)
173 |         return filenames
174 |
175 |     def _create_config_yaml(self, dict_file: Dict[str, str]) -> None:
176 |         """
177 |         Creates a yaml file in dir (can be a temporary dir for tests).
178 |         """
179 |         filename = self.tempdir + "/config_test.yaml"
180 |         with open(filename, "w") as file:
181 |             yaml.dump(dict_file, file, default_flow_style=False)
182 |


--------------------------------------------------------------------------------
/demos/offline_ivf/utils.py:
--------------------------------------------------------------------------------
 1 | # Copyright (c) Meta Platforms, Inc. and affiliates.
 2 | #
 3 | # This source code is licensed under the MIT license found in the
 4 | # LICENSE file in the root directory of this source tree.
 5 |
 6 | import numpy as np
 7 | import os
 8 | from typing import Dict
 9 | import yaml
10 | import faiss
11 | from faiss.contrib.datasets import SyntheticDataset
12 |
13 |
14 | def load_config(config):
15 |     assert os.path.exists(config)
16 |     with open(config, "r") as f:
17 |         return yaml.safe_load(f)
18 |
19 |
20 | def faiss_sanity_check():
21 |     ds = SyntheticDataset(256, 0, 100, 100)
22 |     xq = ds.get_queries()
23 |     xb = ds.get_database()
24 |     index_cpu = faiss.IndexFlat(ds.d)
25 |     index_gpu = faiss.index_cpu_to_all_gpus(index_cpu)
26 |     index_cpu.add(xb)
27 |     index_gpu.add(xb)
28 |     D_cpu, I_cpu = index_cpu.search(xq, 10)
29 |     D_gpu, I_gpu = index_gpu.search(xq, 10)
30 |     assert np.all(I_cpu == I_gpu), "faiss sanity check failed"
31 |     assert np.all(np.isclose(D_cpu, D_gpu)), "faiss sanity check failed"
32 |
33 |
34 | def margin(sample, idx_a, idx_b, D_a_b, D_a, D_b, k, k_extract, threshold):
35 |     """
36 |     two datasets: xa, xb; n = number of pairs
37 |     idx_a - (np,) - query vector ids in xa
38 |     idx_b - (np,) - query vector ids in xb
39 |     D_a_b - (np,) - pairwise distances between xa[idx_a] and xb[idx_b]
40 |     D_a - (np, k) - distances between vectors xa[idx_a] and corresponding nearest neighbours in xb
41 |     D_b - (np, k) - distances between vectors xb[idx_b] and corresponding nearest neighbours in xa
42 |     k - k nearest neighbours used for margin
43 |     k_extract - number of nearest neighbours of each query in xb we consider for margin calculation and filtering
44 |     threshold - margin threshold
45 |     """
46 |
47 |     n = sample
48 |     nk = n * k_extract
49 |     assert idx_a.shape == (n,)
50 |     idx_a_k = idx_a.repeat(k_extract)
51 |     assert idx_a_k.shape == (nk,)
52 |     assert idx_b.shape == (nk,)
53 |     assert D_a_b.shape == (nk,)
54 |     assert D_a.shape == (n, k)
55 |     assert D_b.shape == (nk, k)
56 |     mean_a = np.mean(D_a, axis=1)
57 |     assert mean_a.shape == (n,)
58 |     mean_a_k = mean_a.repeat(k_extract)
59 |     assert mean_a_k.shape == (nk,)
60 |     mean_b = np.mean(D_b, axis=1)
61 |     assert mean_b.shape == (nk,)
62 |     margin = 2 * D_a_b / (mean_a_k + mean_b)
63 |     above_threshold = margin > threshold
64 |     print(np.count_nonzero(above_threshold))
65 |     print(idx_a_k[above_threshold])
66 |     print(idx_b[above_threshold])
67 |     print(margin[above_threshold])
68 |     return margin
69 |
70 |
71 | def add_group_args(group, *args, **kwargs):
72 |     return group.add_argument(*args, **kwargs)
73 |
74 |
75 | def get_intersection_cardinality_frequencies(
76 |     I: np.ndarray, I_gt: np.ndarray
77 | ) -> Dict[int, int]:
78 |     """
79 |     Computes the frequencies for the cardinalities of the intersection of neighbour indices.
80 |     """
81 |     nq = I.shape[0]
82 |     res = []
83 |     for ell in range(nq):
84 |         res.append(len(np.intersect1d(I[ell, :], I_gt[ell, :])))
85 |     values, counts = np.unique(res, return_counts=True)
86 |     return dict(zip(values, counts))
87 |
88 |
89 | def is_pretransform_index(index):
90 |     if index.__class__ == faiss.IndexPreTransform:
91 |         assert hasattr(index, "chain")
92 |         return True
93 |     else:
94 |         assert not hasattr(index, "chain")
95 |         return False
96 |


--------------------------------------------------------------------------------


# Copyright (c) Meta Platforms, Inc. and affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

""" a few tests for graph-based indices (HNSW, nndescent and NSG)"""

import numpy as np
import unittest
import faiss
import tempfile
import os

from common_faiss_tests import get_dataset_2


class TestHNSW(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)
        d = 32
        nt = 0
        nb = 1500
        nq = 500

        (_, self.xb, self.xq) = get_dataset_2(d, nt, nb, nq)
        index = faiss.IndexFlatL2(d)
        index.add(self.xb)
        Dref, Iref = index.search(self.xq, 1)
        self.Iref = Iref

    def test_hnsw(self):
        d = self.xq.shape[1]

        index = faiss.IndexHNSWFlat(d, 16)
        index.add(self.xb)
        Dhnsw, Ihnsw = index.search(self.xq, 1)

        self.assertGreaterEqual((self.Iref == Ihnsw).sum(), 460)

        self.io_and_retest(index, Dhnsw, Ihnsw)

    def test_range_search(self):
        index_flat = faiss.IndexFlat(self.xb.shape[1])
        index_flat.add(self.xb)
        D, _ = index_flat.search(self.xq, 10)
        radius = np.median(D[:, -1])
        lims_ref, Dref, Iref = index_flat.range_search(self.xq, radius)

        index = faiss.IndexHNSWFlat(self.xb.shape[1], 16)
        index.add(self.xb)
        lims, D, I = index.range_search(self.xq, radius)

        nmiss = 0
        # check if returned resutls are a subset of the reference results
        for i in range(len(self.xq)):
            ref = Iref[lims_ref[i]: lims_ref[i + 1]]
            new = I[lims[i]: lims[i + 1]]
            self.assertLessEqual(set(new), set(ref))
            nmiss += len(ref) - len(new)
        # currenly we miss 405 / 6019 neighbors
        self.assertLessEqual(nmiss, lims_ref[-1] * 0.1)

    def test_hnsw_unbounded_queue(self):
        d = self.xq.shape[1]

        index = faiss.IndexHNSWFlat(d, 16)
        index.add(self.xb)
        index.search_bounded_queue = False
        Dhnsw, Ihnsw = index.search(self.xq, 1)

        self.assertGreaterEqual((self.Iref == Ihnsw).sum(), 460)

        self.io_and_retest(index, Dhnsw, Ihnsw)

    def test_hnsw_no_init_level0(self):
        d = self.xq.shape[1]

        index = faiss.IndexHNSWFlat(d, 16)
        index.init_level0 = False
        index.add(self.xb)
        Dhnsw, Ihnsw = index.search(self.xq, 1)

        # This is expected to be smaller because we are not initializing
        # vectors into level 0.
        self.assertGreaterEqual((self.Iref == Ihnsw).sum(), 25)

        self.io_and_retest(index, Dhnsw, Ihnsw)

    def io_and_retest(self, index, Dhnsw, Ihnsw):
        index2 = faiss.deserialize_index(faiss.serialize_index(index))
        Dhnsw2, Ihnsw2 = index2.search(self.xq, 1)

        self.assertTrue(np.all(Dhnsw2 == Dhnsw))
        self.assertTrue(np.all(Ihnsw2 == Ihnsw))

        # also test clone
        index3 = faiss.clone_index(index)
        Dhnsw3, Ihnsw3 = index3.search(self.xq, 1)

        self.assertTrue(np.all(Dhnsw3 == Dhnsw))
        self.assertTrue(np.all(Ihnsw3 == Ihnsw))

    def test_hnsw_2level(self):
        d = self.xq.shape[1]

        quant = faiss.IndexFlatL2(d)

        index = faiss.IndexHNSW2Level(quant, 256, 8, 8)
        index.train(self.xb)
        index.add(self.xb)
        Dhnsw, Ihnsw = index.search(self.xq, 1)

        self.assertGreaterEqual((self.Iref == Ihnsw).sum(), 307)

        self.io_and_retest(index, Dhnsw, Ihnsw)

    def test_hnsw_2level_mixed_search(self):
        d = self.xq.shape[1]

        quant = faiss.IndexFlatL2(d)

        storage = faiss.IndexIVFPQ(quant, d, 32, 8, 8)
        storage.make_direct_map()
        index = faiss.IndexHNSW2Level(quant, 32, 8, 8)
        index.storage = storage
        index.train(self.xb)
        index.add(self.xb)
        Dhnsw, Ihnsw = index.search(self.xq, 1)

        # It is expected that the mixed search will perform worse.
        self.assertGreaterEqual((self.Iref == Ihnsw).sum(), 200)

        self.io_and_retest(index, Dhnsw, Ihnsw)

    def test_add_0_vecs(self):
        index = faiss.IndexHNSWFlat(10, 16)
        zero_vecs = np.zeros((0, 10), dtype='float32')
        # infinite loop
        index.add(zero_vecs)

    def test_hnsw_IP(self):
        d = self.xq.shape[1]

        index_IP = faiss.IndexFlatIP(d)
        index_IP.add(self.xb)
        Dref, Iref = index_IP.search(self.xq, 1)

        index = faiss.IndexHNSWFlat(d, 16, faiss.METRIC_INNER_PRODUCT)
        index.add(self.xb)
        Dhnsw, Ihnsw = index.search(self.xq, 1)

        self.assertGreaterEqual((Iref == Ihnsw).sum(), 470)

        mask = Iref[:, 0] == Ihnsw[:, 0]
        assert np.allclose(Dref[mask, 0], Dhnsw[mask, 0])

    def test_ndis_stats(self):
        d = self.xq.shape[1]

        index = faiss.IndexHNSWFlat(d, 16)
        index.add(self.xb)
        stats = faiss.cvar.hnsw_stats
        stats.reset()
        Dhnsw, Ihnsw = index.search(self.xq, 1)
        self.assertGreater(stats.ndis, len(self.xq) * index.hnsw.efSearch)

    def test_io_no_storage(self):
        d = self.xq.shape[1]
        index = faiss.IndexHNSWFlat(d, 16)
        index.add(self.xb)

        Dref, Iref = index.search(self.xq, 5)

        # test writing without storage
        index2 = faiss.deserialize_index(
            faiss.serialize_index(index, faiss.IO_FLAG_SKIP_STORAGE)
        )
        self.assertEqual(index2.storage, None)
        self.assertRaises(
            RuntimeError,
            index2.search, self.xb, 1)

        # make sure we can store an index with empty storage
        index4 = faiss.deserialize_index(
            faiss.serialize_index(index2))

        # add storage afterwards
        index.storage = faiss.clone_index(index.storage)
        index.own_fields = True

        Dnew, Inew = index.search(self.xq, 5)
        np.testing.assert_array_equal(Dnew, Dref)
        np.testing.assert_array_equal(Inew, Iref)

        if False:
            # test reading without storage
            # not implemented because it is hard to skip over an index
            index3 = faiss.deserialize_index(
                faiss.serialize_index(index), faiss.IO_FLAG_SKIP_STORAGE
            )
            self.assertEqual(index3.storage, None)

    def test_abs_inner_product(self):
        """Test HNSW with abs inner product (not a real distance, so dubious that triangular inequality works)"""
        d = self.xq.shape[1]
        xb = self.xb - self.xb.mean(axis=0)  # need to be centered to give interesting directions
        xq = self.xq - self.xq.mean(axis=0)
        Dref, Iref = faiss.knn(xq, xb, 10, faiss.METRIC_ABS_INNER_PRODUCT)

        index = faiss.IndexHNSWFlat(d, 32, faiss.METRIC_ABS_INNER_PRODUCT)
        index.add(xb)
        Dnew, Inew = index.search(xq, 10)

        inter = faiss.eval_intersection(Iref, Inew)
        # 4769 vs. 500*10
        self.assertGreater(inter, Iref.size * 0.9)

    def test_hnsw_reset(self):
        d = self.xb.shape[1]
        index_flat = faiss.IndexFlat(d)
        index_flat.add(self.xb)
        self.assertEqual(index_flat.ntotal, self.xb.shape[0])
        index_hnsw = faiss.IndexHNSW(index_flat)
        index_hnsw.add(self.xb)
        # * 2 because we add to storage twice. This is just for testing
        # that storage gets cleared correctly.
        self.assertEqual(index_hnsw.ntotal, self.xb.shape[0] * 2)

        index_hnsw.reset()

        self.assertEqual(index_flat.ntotal, 0)
        self.assertEqual(index_hnsw.ntotal, 0)

class Issue3684(unittest.TestCase):

    def test_issue3684(self):
        np.random.seed(1234)  # For reproducibility
        d = 256  # Example dimension
        nb = 10  # Number of database vectors
        nq = 2   # Number of query vectors
        xb = np.random.random((nb, d)).astype('float32')
        xq = np.random.random((nq, d)).astype('float32')

        faiss.normalize_L2(xb)  # Normalize both query and database vectors
        faiss.normalize_L2(xq)

        hnsw_index_ip = faiss.IndexHNSWFlat(256, 16, faiss.METRIC_INNER_PRODUCT)
        hnsw_index_ip.hnsw.efConstruction = 512
        hnsw_index_ip.hnsw.efSearch = 512
        hnsw_index_ip.add(xb)

        # test knn
        D, I = hnsw_index_ip.search(xq, 10)
        self.assertTrue(np.all(D[:, :-1] >= D[:, 1:]))

        # test range search
        radius = 0.74  # Cosine similarity threshold
        lims, D, I = hnsw_index_ip.range_search(xq, radius)
        self.assertTrue(np.all(D >= radius))


class TestNSG(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)
        d = 32
        nt = 0
        nb = 1500
        nq = 500
        self.GK = 32

        _, self.xb, self.xq = get_dataset_2(d, nt, nb, nq)

    def make_knn_graph(self, metric):
        n = self.xb.shape[0]
        d = self.xb.shape[1]
        index = faiss.IndexFlat(d, metric)
        index.add(self.xb)
        _, I = index.search(self.xb, self.GK + 1)
        knn_graph = np.zeros((n, self.GK), dtype=np.int64)

        # For the inner product distance, the distance between a vector and
        # itself may not be the smallest, so it is not guaranteed that I[:, 0]
        # is the query itself.
        for i in range(n):
            cnt = 0
            for j in range(self.GK + 1):
                if I[i, j] != i:
                    knn_graph[i, cnt] = I[i, j]
                    cnt += 1
                if cnt == self.GK:
                    break
        return knn_graph

    def subtest_io_and_clone(self, index, Dnsg, Insg):
        fd, tmpfile = tempfile.mkstemp()
        os.close(fd)
        try:
            faiss.write_index(index, tmpfile)
            index2 = faiss.read_index(tmpfile)
        finally:
            if os.path.exists(tmpfile):
                os.unlink(tmpfile)

        Dnsg2, Insg2 = index2.search(self.xq, 1)
        np.testing.assert_array_equal(Dnsg2, Dnsg)
        np.testing.assert_array_equal(Insg2, Insg)

        # also test clone
        index3 = faiss.clone_index(index)
        Dnsg3, Insg3 = index3.search(self.xq, 1)
        np.testing.assert_array_equal(Dnsg3, Dnsg)
        np.testing.assert_array_equal(Insg3, Insg)

    def subtest_connectivity(self, index, nb):
        vt = faiss.VisitedTable(nb)
        count = index.nsg.dfs(vt, index.nsg.enterpoint, 0)
        self.assertEqual(count, nb)

    def subtest_add(self, build_type, thresh, metric=faiss.METRIC_L2):
        d = self.xq.shape[1]
        metrics = {faiss.METRIC_L2: 'L2',
                   faiss.METRIC_INNER_PRODUCT: 'IP'}

        flat_index = faiss.IndexFlat(d, metric)
        flat_index.add(self.xb)
        Dref, Iref = flat_index.search(self.xq, 1)

        index = faiss.IndexNSGFlat(d, 16, metric)
        index.verbose = True
        index.build_type = build_type
        index.GK = self.GK
        index.add(self.xb)
        Dnsg, Insg = index.search(self.xq, 1)

        recalls = (Iref == Insg).sum()
        self.assertGreaterEqual(recalls, thresh)
        self.subtest_connectivity(index, self.xb.shape[0])
        self.subtest_io_and_clone(index, Dnsg, Insg)

    def subtest_build(self, knn_graph, thresh, metric=faiss.METRIC_L2):
        d = self.xq.shape[1]
        metrics = {faiss.METRIC_L2: 'L2',
                   faiss.METRIC_INNER_PRODUCT: 'IP'}

        flat_index = faiss.IndexFlat(d, metric)
        flat_index.add(self.xb)
        Dref, Iref = flat_index.search(self.xq, 1)

        index = faiss.IndexNSGFlat(d, 16, metric)
        index.verbose = True

        index.build(self.xb, knn_graph)
        Dnsg, Insg = index.search(self.xq, 1)

        recalls = (Iref == Insg).sum()
        self.assertGreaterEqual(recalls, thresh)
        self.subtest_connectivity(index, self.xb.shape[0])

    def test_add_bruteforce_L2(self):
        self.subtest_add(0, 475, faiss.METRIC_L2)

    def test_add_nndescent_L2(self):
        self.subtest_add(1, 475, faiss.METRIC_L2)

    def test_add_bruteforce_IP(self):
        self.subtest_add(0, 480, faiss.METRIC_INNER_PRODUCT)

    def test_add_nndescent_IP(self):
        self.subtest_add(1, 480, faiss.METRIC_INNER_PRODUCT)

    def test_build_L2(self):
        knn_graph = self.make_knn_graph(faiss.METRIC_L2)
        self.subtest_build(knn_graph, 475, faiss.METRIC_L2)

    def test_build_IP(self):
        knn_graph = self.make_knn_graph(faiss.METRIC_INNER_PRODUCT)
        self.subtest_build(knn_graph, 480, faiss.METRIC_INNER_PRODUCT)

    def test_build_invalid_knng(self):
        """Make some invalid entries in the input knn graph.

        It would cause a warning but IndexNSG should be able
        to handle this.
        """
        knn_graph = self.make_knn_graph(faiss.METRIC_L2)
        knn_graph[:100, 5] = -111
        self.subtest_build(knn_graph, 475, faiss.METRIC_L2)

        knn_graph = self.make_knn_graph(faiss.METRIC_INNER_PRODUCT)
        knn_graph[:100, 5] = -111
        self.subtest_build(knn_graph, 480, faiss.METRIC_INNER_PRODUCT)

    def test_reset(self):
        """test IndexNSG.reset()"""
        d = self.xq.shape[1]
        metrics = {faiss.METRIC_L2: 'L2',
                   faiss.METRIC_INNER_PRODUCT: 'IP'}

        metric = faiss.METRIC_L2
        flat_index = faiss.IndexFlat(d, metric)
        flat_index.add(self.xb)
        Dref, Iref = flat_index.search(self.xq, 1)

        index = faiss.IndexNSGFlat(d, 16)
        index.verbose = True
        index.GK = 32

        index.add(self.xb)
        Dnsg, Insg = index.search(self.xq, 1)
        recalls = (Iref == Insg).sum()
        self.assertGreaterEqual(recalls, 475)
        self.subtest_connectivity(index, self.xb.shape[0])

        index.reset()
        index.add(self.xb)
        Dnsg, Insg = index.search(self.xq, 1)
        recalls = (Iref == Insg).sum()
        self.assertGreaterEqual(recalls, 475)
        self.subtest_connectivity(index, self.xb.shape[0])

    def test_order(self):
        """make sure that output results are sorted"""
        d = self.xq.shape[1]
        index = faiss.IndexNSGFlat(d, 32)

        index.train(self.xb)
        index.add(self.xb)

        k = 10
        nq = self.xq.shape[0]
        D, _ = index.search(self.xq, k)

        indices = np.argsort(D, axis=1)
        gt = np.arange(0, k)[np.newaxis, :]  # [1, k]
        gt = np.repeat(gt, nq, axis=0)  # [nq, k]
        np.testing.assert_array_equal(indices, gt)

    def test_nsg_pq(self):
        """Test IndexNSGPQ"""
        d = self.xq.shape[1]
        R, pq_M = 32, 4
        index = faiss.index_factory(d, f"NSG{R}_PQ{pq_M}np")
        assert isinstance(index, faiss.IndexNSGPQ)
        idxpq = faiss.downcast_index(index.storage)
        assert index.nsg.R == R and idxpq.pq.M == pq_M

        flat_index = faiss.IndexFlat(d)
        flat_index.add(self.xb)
        Dref, Iref = flat_index.search(self.xq, k=1)

        index.GK = 32
        index.train(self.xb)
        index.add(self.xb)
        D, I = index.search(self.xq, k=1)

        # test accuracy
        recalls = (Iref == I).sum()
        self.assertGreaterEqual(recalls, 190)  # 193

        # test I/O
        self.subtest_io_and_clone(index, D, I)

    def test_nsg_sq(self):
        """Test IndexNSGSQ"""
        d = self.xq.shape[1]
        R = 32
        index = faiss.index_factory(d, f"NSG{R}_SQ8")
        assert isinstance(index, faiss.IndexNSGSQ)
        idxsq = faiss.downcast_index(index.storage)
        assert index.nsg.R == R
        assert idxsq.sq.qtype == faiss.ScalarQuantizer.QT_8bit

        flat_index = faiss.IndexFlat(d)
        flat_index.add(self.xb)
        Dref, Iref = flat_index.search(self.xq, k=1)

        index.train(self.xb)
        index.add(self.xb)
        D, I = index.search(self.xq, k=1)

        # test accuracy
        recalls = (Iref == I).sum()
        self.assertGreaterEqual(recalls, 405)  # 411

        # test I/O
        self.subtest_io_and_clone(index, D, I)


class TestNNDescent(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)
        d = 32
        nt = 0
        nb = 1500
        nq = 500
        self.GK = 32

        _, self.xb, self.xq = get_dataset_2(d, nt, nb, nq)

    def test_nndescentflat(self):
        d = self.xq.shape[1]
        index = faiss.IndexNNDescentFlat(d, 32)
        index.nndescent.search_L = 8

        flat_index = faiss.IndexFlat(d)
        flat_index.add(self.xb)
        Dref, Iref = flat_index.search(self.xq, k=1)

        index.train(self.xb)
        index.add(self.xb)
        D, I = index.search(self.xq, k=1)

        # test accuracy
        recalls = (Iref == I).sum()
        self.assertGreaterEqual(recalls, 450)  # 462

        # do some IO tests
        fd, tmpfile = tempfile.mkstemp()
        os.close(fd)
        try:
            faiss.write_index(index, tmpfile)
            index2 = faiss.read_index(tmpfile)
        finally:
            if os.path.exists(tmpfile):
                os.unlink(tmpfile)

        D2, I2 = index2.search(self.xq, 1)
        np.testing.assert_array_equal(D2, D)
        np.testing.assert_array_equal(I2, I)

        # also test clone
        index3 = faiss.clone_index(index)
        D3, I3 = index3.search(self.xq, 1)
        np.testing.assert_array_equal(D3, D)
        np.testing.assert_array_equal(I3, I)

    def test_order(self):
        """make sure that output results are sorted"""
        d = self.xq.shape[1]
        index = faiss.IndexNNDescentFlat(d, 32)

        index.train(self.xb)
        index.add(self.xb)

        k = 10
        nq = self.xq.shape[0]
        D, _ = index.search(self.xq, k)

        indices = np.argsort(D, axis=1)
        gt = np.arange(0, k)[np.newaxis, :]  # [1, k]
        gt = np.repeat(gt, nq, axis=0)  # [nq, k]
        np.testing.assert_array_equal(indices, gt)


class TestNNDescentKNNG(unittest.TestCase):

    def test_knng_L2(self):
        self.subtest(32, 10, faiss.METRIC_L2)

    def test_knng_IP(self):
        self.subtest(32, 10, faiss.METRIC_INNER_PRODUCT)

    def subtest(self, d, K, metric):
        metric_names = {faiss.METRIC_L1: 'L1',
                        faiss.METRIC_L2: 'L2',
                        faiss.METRIC_INNER_PRODUCT: 'IP'}

        nb = 1000
        _, xb, _ = get_dataset_2(d, 0, nb, 0)

        _, knn = faiss.knn(xb, xb, K + 1, metric)
        knn = knn[:, 1:]

        index = faiss.IndexNNDescentFlat(d, K, metric)
        index.nndescent.S = 10
        index.nndescent.R = 32
        index.nndescent.L = K + 20
        index.nndescent.iter = 5
        index.verbose = True

        index.add(xb)
        graph = index.nndescent.final_graph
        graph = faiss.vector_to_array(graph)
        graph = graph.reshape(nb, K)

        recalls = 0
        for i in range(nb):
            for j in range(K):
                for k in range(K):
                    if graph[i, j] == knn[i, k]:
                        recalls += 1
                        break
        recall = 1.0 * recalls / (nb * K)
        assert recall > 0.99

    def test_small_nndescent(self):
        """ building a too small graph used to crash, make sure it raises
        an exception instead.
        TODO: build the exact knn graph for small cases
        """
        d = 32
        K = 10
        index = faiss.IndexNNDescentFlat(d, K, faiss.METRIC_L2)
        index.nndescent.S = 10
        index.nndescent.R = 32
        index.nndescent.L = K + 20
        index.nndescent.iter = 5
        index.verbose = True

        xb = np.zeros((78, d), dtype='float32')
        self.assertRaises(RuntimeError, index.add, xb)
